import numpy as np
import cv2
#import motor

#細かいノイズを除去するために画像を圧縮
def mosaic(original_img, ratio=0.1):
    small_img = cv2.resize(original_img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small_img, original_img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

#赤色検出
def detect_red(small_img):
    # HSV色空間に変換
    hsv_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2HSV)
    
    # 赤色のHSVの値域1
    red_min = np.array([0,64,0])
    red_max = np.array([30,255,255])
    mask1 = cv2.inRange(hsv_img, red_min, red_max)
    
    # 赤色のHSVの値域2
    red_min = np.array([150,127,0])
    red_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv_img, red_min, red_max)
    
    mask = mask1 + mask2

    masked_img = cv2.bitwise_and(small_img, small_img, mask=mask)
    return mask, masked_img

#赤色の重心を求める
def get_center(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #最大の輪郭を抽出
    max_contour = max(contours, key = cv2.contourArea)

    #最大輪郭の重心を求める
    # 重心の計算
    m = cv2.moments(max_contour)
    cx,cy= m['m10']/m['m00'] , m['m01']/m['m00']
    print(f"Weight Center = ({cx}, {cy})")
    # 座標を四捨五入
    cx, cy = round(cx), round(cy)
    # 重心位置に x印を書く
    cv2.line(original_img, (cx-5,cy-5), (cx+5,cy+5), (0, 255, 0), 2)
    cv2.line(original_img, (cx+5,cy-5), (cx-5,cy+5), (0, 255, 0), 2)

    cv2.drawContours(original_img, [max_contour], -1, (0, 255, 0), thickness=2)

    return original_img, max_contour, cx, cy

def get_area(max_contour):
    #輪郭の面積を計算
    area = cv2.contourArea(max_contour)
    img_area = original_img.shape[0] * original_img.shape[1] #画像の縦横の積
    area_ratio = area / img_area * 100 #面積の割合を計算
    if area_ratio < 1.0:
        area_ratio = 0.0
    print(f"Area ratio = {area_ratio:.1f}%")
    return area_ratio

def get_angle(cx, cy):
    #重心から現在位置とゴールの相対角度を大まかに計算
    img_width = original_img.shape[1]
    quat_width = img_width / 5
    x0, x1, x2, x3, x4, x5 = 0, quat_width, quat_width*2, quat_width*3, quat_width*4, quat_width*5

    if x0 < cx <x1:
        angle = 1
    elif x1 < cx < x2:
        angle = 2
    elif x2 < cx < x3:
        angle = 3
    elif x3 < cx < x4:
        angle = 4
    elif x4 < cx < x5:
        angle = 5
    
    print("angle = ", angle)

    return angle

def image_guided_driving(angle, area_ratio):

    area_ratio = get_area(max_contour)

    while area_ratio == 0:
        print("ゴールが見つかりません。回転します。")
        motor.move(40, -40, 0.1)
        motor.stop(0.1)
        area_ratio = get_area(max_contour)
    print("ゴールを捉えました。ゴールへ向かいます。")
    
    while area_ratio < 80:
        #cansatの真正面にゴールがないとき
        while angle =! 3:
            if angle == 1:
                motor.move(-20, 20, 0.5)
            elif angle == 2:
                motor.move(-20, 20, 0,3)
            elif angle == 4:
                motor.move(20, -20, 0.3)
            elif angle == 5:
                motor.move(20, -20, 0.5)

        #cansatの真正面にゴールがあるとき
        if 60 < area_ratio <= 80:
            t_running = 0.5
        elif 40 < area_ratio <= 60:
            t_running = 0.3
        elif 0 < area_ratio <= 40:
            t_running = 0.1
        
        motor.move(30, 30, t_running)
        motor.decelaration(10, 10)
        motor.motor_stop(1)

        area_ratio = get_area(max_contour)
    

    print("目的地周辺に到着しました。案内を終了します。")
    print("お疲れさまでした。")
    



if __name__ == "__main__":
    original_img = cv2.imread('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\ImageGuide-0002.jpg')
    mosaic_img = mosaic(original_img)
    cv2.imshow('mosaic', mosaic_img)
    
    #画僧の保存
    cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\mosaic.jpg', mosaic_img)
    
    mask, masked_img = detect_red(mosaic_img)
    cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\masked_img.jpg', masked_img)

    #対象物とその重心を描画した画像を保存
    original_img, max_contour, cx, cy = get_center(mask)
    cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\max_contour.jpg', original_img)

    #赤色が占める割合を計算
    get_area(max_contour)

    get_angle(cx,cy)
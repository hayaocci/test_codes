import numpy as np
import cv2



#濃淡画像のノイズ処理
#def noise_reduction(img):
    

#BGR色検知 (opencvではRGBではなくBGRであることに注意)
# def BGR_detect(img, BGR, threshold):
#     #BGRの値を取得
#     bgr = img[BGR[0], BGR[1]]
#     #print(bgr)
#     #BGRの値を閾値で比較
#     if bgr[0] > threshold[0] and bgr[1] > threshold[1] and bgr[2] > threshold[2]:
#         return True
#     else:
#         return False

original_img = cv2.imread('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\ImageGuide-0153.jpg')

def mosaic(original_img, ratio=0.05):
    small_img = cv2.resize(original_img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small_img, original_img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

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

def get_contours(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #最大の輪郭を抽出
    max_contour = max(contours, key = cv2.contourArea)

    #最大輪郭の重心を求める
    # 重心の計算
    m = cv2.moments(max_contour)
    x,y= m['m10']/m['m00'] , m['m01']/m['m00']
    print(f"Weight Center = ({x}, {y})")
    # 座標を四捨五入
    x, y = round(x), round(y)
    # 重心位置に x印を書く
    cv2.line(original_img, (x-5,y-5), (x+5,y+5), (0, 0, 255), 2)
    cv2.line(original_img, (x+5,y-5), (x-5,y+5), (0, 0, 255), 2)

    cv2.drawContours(original_img, [max_contour], -1, (0, 0, 255), thickness=2)



    return original_img
    '''
    max_contour = max(contours, key=lambda x: cv2.contourArea(x))

    # 全ての輪郭を描画
    cv2.drawContours(original_img, [max_contour], -1, (0, 0, 255), thickness=2)

    # 輪郭の点の描画
    for contour in contours:
        for point in contour:
            cv2.circle(original_img, point[0], 3, (0, 255, 0), -1)
    
        #一つ以上検出
        if len(contours) > 0:
            for cnt in contours:
                # 最小外接円を描く
                (x,y), radius = cv2.minEnclosingCircle(cnt)
                center = (int(x),int(y))
                radius = int(radius)
 
                if radius > r:
                    radius_frame = cv2.circle(masked_img,center,radius,(0,255,0),2)
         
    return original_img, radius_frame
    '''
if __name__ == "__main__":
    mosaic_img = mosaic(original_img)
    cv2.imshow('mosaic', mosaic_img)
    
    #画僧の保存
    cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\mosaic.jpg', mosaic_img)
    
    mask, masked_img = detect_red(mosaic_img)
    cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\masked_img.jpg', masked_img)

    get_contours(mask)

    original_img = get_contours(mask)
    cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\max_contour.jpg', original_img)


    # r = 10
    # original_img, radius_frame = get_contours(mask)
    # cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\max_contour.jpg', original_img)
    # cv2.imwrite('C:\\Users\\taguc\\workspace_cansat\\goal_imgs\\contours.jpg', radius_frame)
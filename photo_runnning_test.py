import numpy as np
import cv2




#濃淡画像のノイズ処理
def noise_reduction(img):
    

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

original_img = cv2.imread('')

def mosaic(original_img, ratio):
    small_img = cv2.resize(original_img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small_img, original_img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
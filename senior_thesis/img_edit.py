import cv2

# resize image
def resize_img(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)

# 画面の中央の正方形を切り取る
def crop_center(img):
    height, width = img.shape[:2]
    if height > width:
        y = int((height - width) / 2)
        return img[y:y+width, 0:width]
    else:
        x = int((width - height) / 2)
        return img[0:height, x:x+height]

if __name__ == "__main__":
    img = cv2.imread('earth_img_1.jpg')

    img = crop_center(img)

    img = resize_img(img, 40, 40)
    cv2.imwrite('resized_img.jpg', img)


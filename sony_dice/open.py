import numpy as np
import matplotlib.pyplot as plt

# .npyファイルのパスを指定
file_path = "X_test.npy"  # ファイルパスを実際のファイルに置き換えてください

# .npyファイルを読み込む
data = np.load(file_path)

# データの形状を確認
data_shape = data.shape

# 20x20の画像に分割する
num_images = data_shape[1]  # 画像の枚数
image_size = 20  # 画像のサイズ（20x20）

i = 0
# 最初の画像を取得
while True:
    first_image = data[i]

    # 20x20の画像に分割
    first_image = first_image.reshape(image_size, image_size)

    # 画像を表示
    plt.imshow(first_image, cmap='gray')
    plt.title("dataset no" + str(i)
    plt.show()
    i += 1

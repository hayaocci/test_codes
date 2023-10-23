import numpy as np
from PIL import Image

# .npyファイルのパスを指定
file_path = "X_test.npy"  # 実際の.npyファイルのパスに置き換えてください

# .npyファイルを読み込む
data = np.load(file_path)

# 20x20の画像に分割する
image_size = 20  # 画像のサイズ（20x20）
num_images = data.shape[0]  # 画像の枚数

# 画像を順に保存
for i in range(num_images):
    image_data = data[i].reshape(image_size, image_size)
    image = Image.fromarray(image_data.astype('uint8'))  # 変換不要
    image_path = f"test/{i}.png"  # 保存先のフォルダを指定
    image.save(image_path)

print(f"{num_images} 画像をJPEGファイルに test フォルダに保存しました。")

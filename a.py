    photo_take = picture(file_name, 320, 240)
    print("撮影した写真のファイルパス：", photo_take)
    
    # 入力ファイルパスと出力ファイルパスを指定してリサイズ
    input_file = photo_take    # 入力ファイルのパスを適切に指定してください
    photo_name = "/home/dendenmushi/cansat2023/sequence/ML_imgs/send_photo_resize.jpg"  # 出力ファイルのパスを適切に指定してください
    new_width = 80            # リサイズ後の幅を指定します
    new_height = 60           # リサイズ後の高さを指定します

    # リサイズを実行
    resize_image(input_file, photo_name, new_width, new_height)
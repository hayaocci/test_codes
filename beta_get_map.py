import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import csv
import math

def get_map(file_path, lat_goal, lon_goal):
    with open(file_path) as f:
        #スペースで区切る
        reader = csv.reader(f, delimiter=',')
        log_data = [row for row in reader]

        #転地行列の取得
        log_data_T = [list(x) for x in zip(*log_data)]

        #-----緯度・経度・方位角の取得-----#
        gps_lat = [float(v) for v in log_data_T[0]]
        gps_lon = [float(v) for v in log_data_T[1]]
        rover_azimuth = [float(v) for v in log_data_T[2]]

        cos_azimuth_array = []
        sin_azimuth_array = []
        for i in range(len(rover_azimuth)-1):
            cos_azimuth = math.cos(rover_azimuth[i])
            sin_azimuth = math.sin(rover_azimuth[i])
            cos_azimuth_array.append(cos_azimuth)
            sin_azimuth_array.append(sin_azimuth)

        cos_azimuth_array[0] = 0
        sin_azimuth_array[0] = 0
        cos_azimuth_array.append(0)
        sin_azimuth_array.append(0)

        #-----描画処理-----#
        #グラフのタイトル
        plt.title("A visualize control record")

        #軸の範囲(少し大き目に設定)
        lim_x1 = min(gps_lat) - 0.000010
        lim_x2 = max(gps_lat) + 0.000010
        lim_y1 = min(gps_lon) - 0.000010
        lim_y2 = max(gps_lon) + 0.000010
        plt.xlim(lim_x1, lim_x2)
        plt.ylim(lim_y1, lim_y2)

        #目盛りの設定
        plt.gca().xaxis.get_major_formatter().set_useOffset(False)
        plt.gca().yaxis.get_major_formatter().set_useOffset(False)

        #軸ラベル
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")

        #座標のプロット
        plt.scatter(gps_lat[0], gps_lon[0], color="blue")
        plt.quiver(gps_lat, gps_lon, cos_azimuth_array, sin_azimuth_array, color="red")
        plt.plot(gps_lat, gps_lon, label="Trajectory", linestyle="dashed", color="black")
        
        #スタート地点、ゴール地点、制御終了地点の座標の表示
        plt.scatter(gps_lat[0], gps_lon[0], color="blue", edgecolors="black")
        plt.scatter(lat_goal, lon_goal, color="red", edgecolors="black")
        plt.scatter(gps_lat[-1], gps_lon[-1], color="red", edgecolors="black")



        #地図の説明
        arrow_dict = dict(arrowstyle="simple", color="gray", connectionstyle="arc3")
        text_dict = text_dict = dict(boxstyle="round",fc="silver", ec="mediumblue")
        plt.annotate("Target point" + "\n" + str(lat_goal) + ", "+ str(lon_goal) + ", "+ "altitude", xy=(lat_goal, lon_goal), xytext=(lat_goal - 0.000025, lon_goal - 0.000020), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control start point" + "\n" + str(gps_lat[0]) + ", "+ str(gps_lon[0]) + ", "+ "altitude", xy=(gps_lat[0], gps_lon[0]), xytext=(gps_lat[0] + 0.000005, gps_lon[0] - 0.000020), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control finish point" + "\n" + str(gps_lat[-1]) + ", "+ str(gps_lon[-1]) + ", "+ "altitude", xy=(gps_lat[-1], gps_lon[-1]), xytext=(gps_lat[-1] - 0.000020, gps_lon[-1] + 0.000009), arrowprops=arrow_dict, bbox=text_dict)
        
        #グリッドの表示
        plt.grid()

        #軸凡例
        plt.legend()

        #地図の保存
        plt.savefig('A visual control record.png', bbox_inches='tight')
        plt.show()

        print(gps_lat)
        print(gps_lon)
        print(rover_azimuth)


        # plt.scatter(gps_lat, gps_lon) #, s=10, c='blue', marker='o', label='rover')
        # plt.show()

    #-----lat, lonの取得-----#
    # for i in range(5):
    #     lat = log_data[i][0]
    #     lon = log_data[i][1]
    #     rover_azimuth = log_data[i][2]
    #     # print(lat, lon, rover_azimuth)
    #     # print(log_data_T[0])


if __name__ == '__main__':
    file_path = 'test_data.csv'
    lat_goal = 35.924425
    lon_goal = 139.912890

    get_map(file_path, lat_goal, lon_goal)
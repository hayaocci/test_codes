import matplotlib.pyplot as plt
import matplotlib.ticker as tickers
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
        plt.title("A visualized control record")

        #軸の範囲(少し大き目に設定)
        lim_x1 = min(gps_lat) - 0.000150
        lim_x2 = max(gps_lat) + 0.000200
        lim_y1 = min(gps_lon) - 0.000150
        lim_y2 = max(gps_lon) + 0.000200
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
        plt.quiver(gps_lat, gps_lon, cos_azimuth_array, sin_azimuth_array, color="red", width=0.003, edgecolor="black", scale=50)
        plt.plot(gps_lat, gps_lon, label="Trajectory", linestyle="dashed", color="black")
        
        #スタート地点、ゴール地点、制御終了地点の座標の表示
        plt.scatter(gps_lat[0], gps_lon[0], color="blue", edgecolors="black")
        plt.scatter(lat_goal, lon_goal, color="red", edgecolors="black")
        plt.scatter(gps_lat[-1], gps_lon[-1], color="red", edgecolors="black")

        #地図の情報を表示
        arrow_dict = dict(arrowstyle="wedge", color="silver", connectionstyle="arc3")
        text_dict = text_dict = dict(boxstyle="round",fc="silver", ec="mediumblue")
        plt.annotate("Target point" + "\n" + str(lat_goal) + ", "+ str(lon_goal) + ", "+ "altitude", xy=(lat_goal, lon_goal), xytext=(lim_x2 - 0.000100, lim_y2 - 0.000900), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control start point" + "\n" + str(gps_lat[0]) + ", "+ str(gps_lon[0]) + ", "+ "altitude", xy=(gps_lat[0], gps_lon[0]), xytext=(lim_x2 - 0.000100, lim_y2 - 0.000300), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control finish point" + "\n" + str(gps_lat[-1]) + ", "+ str(gps_lon[-1]) + ", "+ "altitude", xy=(gps_lat[-1], gps_lon[-1]), xytext=(lim_x2 - 0.000100, lim_y2 - 0.000600), arrowprops=arrow_dict, bbox=text_dict)
        
        #グリッドの表示
        plt.grid()

        #軸凡例
        plt.legend()

        #地図の保存
        plt.savefig('A visualized control record.png', bbox_inches='tight')
        plt.show()

        # print(gps_lat)
        # print(gps_lon)
        # print(rover_azimuth)

        #表の作成
        plt.rcParams['font.family'] = 'Times New Roman'

        fig = plt.figure()
        ax1 = fig.add_subplot(111)

        ax1.axis('off')
        ax1.table(cellText=log_data, colLabels=['Latitude', 'Longtitude', 'theta'], loc='center')

        plt.table(cellText=log_data, loc='center')
        plt.show()


if __name__ == '__main__':
    file_path = 'log_data.csv'
    lat_goal = 35.9242411
    lon_goal = 139.9120618

    get_map(file_path, lat_goal, lon_goal)
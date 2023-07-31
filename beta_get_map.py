import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import math

def get_map(file_path, lat_goal, lon_goal):
    with open(file_path) as f:
        #スペースで区切る
        reader = csv.reader(f, delimiter=',')
        data = [row for row in reader]

        data_2 = [list(x) for x in zip(*data)]
        data_2_lat = [float(v) for v in data_2[0]]
        data_2_lon = [float(v) for v in data_2[1]]
        rover_azimuth = [float(v) for v in data_2[2]]

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

        #軸の範囲
        lim_x1 = min(data_2_lat) - 0.000010
        lim_x2 = max(data_2_lat) + 0.000010
        lim_y1 = min(data_2_lon) - 0.000010
        lim_y2 = max(data_2_lon) + 0.000010
        plt.xlim(lim_x1, lim_x2)
        plt.ylim(lim_y1, lim_y2)

        #軸ラベル
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")


        plt.scatter(data_2_lat[0], data_2_lon[0], color="blue")
        plt.quiver(data_2_lat, data_2_lon, cos_azimuth_array, sin_azimuth_array, color="red")
        plt.plot(data_2_lat, data_2_lon, label="Trajectry", linestyle="dashed", color="black")
        
        #スタート地点、ゴール地点、制御終了地点の座標の表示
        plt.scatter(data_2_lat[0], data_2_lon[0], color="blue", edgecolors="black")
        plt.scatter(lat_goal, lon_goal, color="red", edgecolors="black")
        plt.scatter(data_2_lat[-1], data_2_lon[-1], color="red", edgecolors="black")



        #

        plt.gca().xaxis.get_major_formatter().set_useOffset(False)
        plt.gca().yaxis.get_major_formatter().set_useOffset(False)
        arrow_dict = dict(arrowstyle="simple", color="gray", connectionstyle="arc3")
        text_dict = text_dict = dict(boxstyle="round",fc="silver", ec="mediumblue")
        plt.annotate("Target point" + "\n" + str(lat_goal) + ", "+ str(lon_goal) + ", "+ "altitude", xy=(lat_goal, lon_goal), xytext=(lat_goal - 0.000025, lon_goal - 0.000020), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control start point" + "\n" + str(data_2_lat[0]) + ", "+ str(data_2_lon[0]) + ", "+ "altitude", xy=(data_2_lat[0], data_2_lon[0]), xytext=(data_2_lat[0] + 0.000005, data_2_lon[0] - 0.000020), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control finish point" + "\n" + str(data_2_lat[-1]) + ", "+ str(data_2_lon[-1]) + ", "+ "altitude", xy=(data_2_lat[-1], data_2_lon[-1]), xytext=(data_2_lat[-1] - 0.000020, data_2_lon[-1] + 0.000009), arrowprops=arrow_dict, bbox=text_dict)


        plt.grid()
        #軸凡例
        plt.legend()


        figsize_px = np.array([1000, 800])
        dpi = 100
        figsize_inch = figsize_px / dpi
        plt.figure(figsize=figsize_inch)
        plt.savefig("test.png")

        plt.show()

        print(data_2_lat)
        print(data_2_lon)
        print(rover_azimuth)


        # plt.scatter(data_2_lat, data_2_lon) #, s=10, c='blue', marker='o', label='rover')
        # plt.show()

    #-----lat, lonの取得-----#
    # for i in range(5):
    #     lat = data[i][0]
    #     lon = data[i][1]
    #     rover_azimuth = data[i][2]
    #     # print(lat, lon, rover_azimuth)
    #     # print(data_2[0])


if __name__ == '__main__':
    file_path = 'test_data.csv'
    lat_goal = 35.924425
    lon_goal = 139.912890

    get_map(file_path, lat_goal, lon_goal)
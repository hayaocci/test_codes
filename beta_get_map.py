import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import math

def get_map(file_path):
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
        for i in range(len(rover_azimuth)):
            cos_azimuth = math.cos(rover_azimuth[i])
            sin_azimuth = math.sin(rover_azimuth[i])
            cos_azimuth_array.append(cos_azimuth)
            sin_azimuth_array.append(sin_azimuth)


        #-----描画処理-----#
        #グラフのタイトル
        plt.title("Navigation Trajectry Map")

        #軸ラベル
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")

        #
        plt.scatter(data_2_lat[0], data_2_lon[0], color="blue")
        plt.quiver(data_2_lat, data_2_lon, cos_azimuth_array, sin_azimuth_array, color="red")
        plt.plot(data_2_lat, data_2_lon, label="Trajectry", linestyle="dashed", color="black")
        plt.scatter(data_2_lat[0], data_2_lon[0], color="blue")
        plt.scatter(data_2_lat[-1], data_2_lon[-1], color="red")

        #
        arrow_dict = dict(arrowstyle="simple", color="gray", connectionstyle="arc3")
        text_dict = text_dict = dict(boxstyle="round",fc="silver", ec="mediumblue")
        plt.annotate("Control start point" + "\n" + str(data_2_lat[0]) + ", "+ str(data_2_lat[0]) + ", "+ "altitude", xy=(data_2_lat[0], data_2_lon[0]), xytext=(data_2_lat[0] + 0.000005, data_2_lon[0] - 0.000020), arrowprops=arrow_dict, bbox=text_dict)
        plt.annotate("Control finish point" + "\n" + str(data_2_lat[-1]) + ", "+ str(data_2_lat[-1]) + ", "+ "altitude", xy=(data_2_lat[-1], data_2_lon[-1]), xytext=(data_2_lat[-1] - 0.000020, data_2_lon[-1] + 0.000009), arrowprops=arrow_dict, bbox=text_dict)

        plt.grid()
        #軸凡例
        plt.legend()

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
    get_map(file_path)
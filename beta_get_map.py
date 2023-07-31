import matplotlib.pyplot as plt
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

        plt.quiver(data_2_lat, data_2_lon, cos_azimuth_array, sin_azimuth_array)
        plt.plot(data_2_lat, data_2_lon)
        plt.show()

        print(data_2_lat)
        print(data_2_lon)
        print(rover_azimuth)


        plt.scatter(data_2_lat, data_2_lon) #, s=10, c='blue', marker='o', label='rover')
        plt.show()

    #-----lat, lonの取得-----#
    for i in range(5):
        lat = data[i][0]
        lon = data[i][1]
        rover_azimuth = data[i][2]
        # print(lat, lon, rover_azimuth)
        # print(data_2[0])


if __name__ == '__main__':
    file_path = 'test_data.csv'
    get_map(file_path)
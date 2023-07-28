#PID制御のテストコード

theta_array = []
theta_differential_array = []

def make_theta_array(array: list, array_num: int):
    #-----決められた数の要素を含む空配列の作成-----#

    for i in range(array_num):
        array.append(0)
    
    return array

def theta_array(theta, array:list):
    #-----thetaの値を蓄積する-----#

    #古い要素を消去
    del array[0]

    #新しい要素を追加
    array.append(theta)

    return array

def proportional_control(theta):
    #-----P制御-----#
    
    #比例係数の設定
    Kp = 0.5

    mp = Kp * theta

    return mp

def integral_control(theta_array: list):
    #I制御

    #積分係数の設定
    Ki = 0.5

    #thetaの積分処理
    theta_integral = sum(theta_array)

    mi = Ki * theta_integral

    return mi

def differential_control(theta_array: list):
    #D制御

    #微分係数の設定
    Kd = 0.5

    #thetaの微分処理
    for i in range(len(theta_array)):
        theta_differential = theta_array[i] - theta_array[i-1]
        theta_differential_array.append(theta_differential)

    md = Kd * theta_differential[18]

    return md



if __name__ == "__main__":
    theta = 0.5
    m = proportional_control(theta)
    print(m)

    theta = 0.5
    m = integral_control(theta, theta_array)
    print(m)
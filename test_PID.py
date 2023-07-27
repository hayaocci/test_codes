#PID制御のテストコード

def proportional_control(theta):
    #-----P制御-----#
    
    #比例係数の設定
    Kp = 0.5

    manipulated_variable = Kp * theta

    return manipulated_variable

theta_array = []

def integral_control(theta, theta_array: list):
    #I制御

    #積分係数の設定
    Ki = 0.5

    #thetaの積分処理
    theta_array.append(theta)
    theta_integral = sum(theta_array)

    manipulated_variable = Ki * theta_integral

    return manipulated_variable

def differential_control(theta):
    #D制御

    #微分係数の設定
    Kd = 0.5

    #thetaの微分処理

    manipulated_variable =

    return manipulated_variable

if __name__ == "__main__":
    theta = 0.5
    manipulated_variable = proportional_control(theta)
    print(manipulated_variable)

    theta = 0.5
    manipulated_variable = integral_control(theta, theta_array)
    print(manipulated_variable)
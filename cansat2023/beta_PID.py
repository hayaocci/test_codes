# test_PID.pyの改良版

from collections import deque

class PID_Controller:
    '''
    PID制御を行うクラス
    '''
    def __init__(self, kp, ki, kd, target_azimuth, validate_ki, log_interval):
        '''
        log_interval: 積分する区間の長さ・積分器に利用
        validate_ki: 積分器を利用するまでの長さ
        '''
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target_azimuth = target_azimuth
        self.validate_ki = validate_ki
        self.deviation = deque([0]*log_interval, maxlen=log_interval)
        self.integral = 0
        self.derivative = 0
        self.output = 0
        self.count = 0

    def pid_output(self, rover_azimuth):
        '''
        PID制御を行う
        '''
        
class FunctionCameraSelector:
    def __init__(self, client, sensor_handle):
        self.Client = client
        self.SensorHandle = sensor_handle
        # self.Target_size = target_size
        # self.Channel_gamut = channel_gamut
        # self.Shutter_speed = shutter_speed
        # , target_size, channel_gamut, shutter_speed

    def select_camera_A(self):
        print("选择相机A")
        self.Target_size = 2/3
        self.Channel_gamut = 8
        self.Shutter_speed = 1/50
        print("靶面尺寸：", self.Target_size,
              "通道色域：", self.Channel_gamut,
              "快门速度：", self.Shutter_speed)

    def select_camera_B(self):
        print("选择相机B")
        self.Target_size = 1/1.8
        self.Channel_gamut =8
        self.Shutter_speed = 1/150
        print("靶面尺寸：", self.Target_size,
              "通道色域：", self.Channel_gamut,
              "快门速度：", self.Shutter_speed)

    def select_camera_C(self):
        print("选择相机C")
        self.Target_size = 1/2.8
        self.Channel_gamut = 16
        self.Shutter_speed = 1/500
        print("靶面尺寸：", self.Target_size,
              "通道色域：", self.Channel_gamut,
              "快门速度：", self.Shutter_speed)

    def select_camera(self, option):
        if option == 'A':
            self.select_camera_A()
        elif option == 'B':
            self.select_camera_B()
        elif option == 'C':
            self.select_camera_C()
        else:
            print("无效的选项")

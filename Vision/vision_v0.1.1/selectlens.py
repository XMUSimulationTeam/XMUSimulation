class FunctionLensSelector:
    def __init__(self, client, sensor_handle):
        self.client = client
        self.SensorHandle = sensor_handle

    def select_lens_A(self):
        print("选择镜头A")
        # self.client.simxSetObjectFloatParameter(self.SensorHandle, 1000, 0.01,
        #                                         self.client.simxServiceCall())  # 修改near_clipping_plane值
        # self.client.simxSetObjectFloatParameter(self.SensorHandle, 1001, 1.64,
        #                                         self.client.simxServiceCall())  # 修改far_clipping_plane值
        self.client.simxSetObjectFloatParameter(self.SensorHandle, 1004, 1.7, self.client.simxServiceCall())
        self.client.simxSetObjectIntParameter(self.SensorHandle, 1002, 512,
                                              self.client.simxServiceCall())  # 修改ResolutionX值
        self.client.simxSetObjectIntParameter(self.SensorHandle, 1003, 512,
                                              self.client.simxServiceCall())  # 修改ResolutionY值
        # Near_clipping_plane = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1000,
        #                                                               self.client.simxServiceCall())  # 获取near_clipping_plane
        # Far_clipping_plane = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1001,
        #                                                              self.client.simxServiceCall())  # 获取far_clipping_plane值
        ResolutionX = self.client.simxGetObjectIntParameter(self.SensorHandle, 1002,
                                                            self.client.simxServiceCall())  # 获取ResolutionX值
        ResolutionY = self.client.simxGetObjectIntParameter(self.SensorHandle, 1003,
                                                            self.client.simxServiceCall())  # 获取ResolutionY值
        Perspective_angle = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1004,
                                                                    self.client.simxServiceCall())
        # print('Clipping_plane:', Near_clipping_plane[1], '-', Far_clipping_plane[1])
        print('Resolution:', ResolutionX[1], '*', ResolutionY[1])
        print('Perspective_angle:', Perspective_angle[1])
        # print('SimulationTime:', self.client.simxGetSimulationTime(self.client.simxServiceCall())[1])  # 获取仿真时间
        # print('SimulationTimeStep:', self.client.simxGetSimulationTimeStep(self.client.simxServiceCall())[1])  # 获取仿真步长
        # print('SimulationState:', self.client.simxGetSimulationState(self.client.simxServiceCall())[1])  # 获取仿真状态

    def select_lens_B(self):
        print("选择镜头B")
        # self.client.simxSetObjectFloatParameter(self.SensorHandle, 1000, 0.01,
        #                                         self.client.simxServiceCall())  # 修改near_clipping_plane值
        # self.client.simxSetObjectFloatParameter(self.SensorHandle, 1001, 1.64,
        #                                         self.client.simxServiceCall())  # 修改far_clipping_plane值
        self.client.simxSetObjectFloatParameter(self.SensorHandle, 1004, 1.7, self.client.simxServiceCall())
        self.client.simxSetObjectIntParameter(self.SensorHandle, 1002, 256,
                                              self.client.simxServiceCall())  # 修改ResolutionX值
        self.client.simxSetObjectIntParameter(self.SensorHandle, 1003, 256,
                                              self.client.simxServiceCall())  # 修改ResolutionY值
        # Near_clipping_plane = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1000,
        #                                                               self.client.simxServiceCall())  # 获取near_clipping_plane
        # Far_clipping_plane = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1001,
        #                                                              self.client.simxServiceCall())  # 获取far_clipping_plane值
        ResolutionX = self.client.simxGetObjectIntParameter(self.SensorHandle, 1002,
                                                            self.client.simxServiceCall())  # 获取ResolutionX值
        ResolutionY = self.client.simxGetObjectIntParameter(self.SensorHandle, 1003,
                                                            self.client.simxServiceCall())  # 获取ResolutionY值
        Perspective_angle = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1004,
                                                                    self.client.simxServiceCall())
        # print('Clipping_plane:', Near_clipping_plane[1], '-', Far_clipping_plane[1])
        print('Resolution:', ResolutionX[1], '*', ResolutionY[1])
        print('Perspective_angle:', Perspective_angle[1])
        # print('SimulationTime:', self.client.simxGetSimulationTime(self.client.simxServiceCall())[1])  # 获取仿真时间
        # print('SimulationTimeStep:', self.client.simxGetSimulationTimeStep(self.client.simxServiceCall())[1])  # 获取仿真步长
        # print('SimulationState:', self.client.simxGetSimulationState(self.client.simxServiceCall())[1])  # 获取仿真状态

    def select_lens_C(self):
        print("选择镜头C")
        # self.client.simxSetObjectFloatParameter(self.SensorHandle, 1000, 0.01,
        #                                         self.client.simxServiceCall())  # 修改near_clipping_plane值
        # self.client.simxSetObjectFloatParameter(self.SensorHandle, 1001, 1.64,
        #                                         self.client.simxServiceCall())  # 修改far_clipping_plane值
        self.client.simxSetObjectFloatParameter(self.SensorHandle, 1004, 1, self.client.simxServiceCall())
        self.client.simxSetObjectIntParameter(self.SensorHandle, 1002, 512,
                                              self.client.simxServiceCall())  # 修改ResolutionX值
        self.client.simxSetObjectIntParameter(self.SensorHandle, 1003, 512,
                                              self.client.simxServiceCall())  # 修改ResolutionY值
        # Near_clipping_plane = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1000,
        #                                                               self.client.simxServiceCall())  # 获取near_clipping_plane
        # Far_clipping_plane = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1001,
        #                                                              self.client.simxServiceCall())  # 获取far_clipping_plane值
        ResolutionX = self.client.simxGetObjectIntParameter(self.SensorHandle, 1002,
                                                            self.client.simxServiceCall())  # 获取ResolutionX值
        ResolutionY = self.client.simxGetObjectIntParameter(self.SensorHandle, 1003,
                                                            self.client.simxServiceCall())  # 获取ResolutionY值
        Perspective_angle = self.client.simxGetObjectFloatParameter(self.SensorHandle, 1004,
                                                                    self.client.simxServiceCall())
        # print('Clipping_plane:', Near_clipping_plane[1], '-', Far_clipping_plane[1])
        print('Resolution:', ResolutionX[1], '*', ResolutionY[1])
        print('Perspective_angle:', Perspective_angle[1])
        # print('SimulationTime:', self.client.simxGetSimulationTime(self.client.simxServiceCall())[1])  # 获取仿真时间
        # print('SimulationTimeStep:', self.client.simxGetSimulationTimeStep(self.client.simxServiceCall())[1])  # 获取仿真步长
        # print('SimulationState:', self.client.simxGetSimulationState(self.client.simxServiceCall())[1])  # 获取仿真状态

    def select_lens(self, option):
        if option == 'A':
            self.select_lens_A()
        elif option == 'B':
            self.select_lens_B()
        elif option == 'C':
            self.select_lens_C()
        else:
            print("无效的选项")

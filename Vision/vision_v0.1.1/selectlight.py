import time
class FunctionLightSelector:
    def __init__(self, client, spotlight_handle):
        self.Client = client
        self.SpotlightHandle = spotlight_handle

    def call_vrep_script_function(self, param1, param2, param3):
        args = [param1, param2, param3]
        ret = self.Client.simxCallScriptFunction('myFunctionName@Spotlight', 'sim.scripttype_childscript', args, self.Client.simxServiceCall())
        print(ret)

    def select_light_A(self):
        print("选择光源A")
        # self.Client.simxSetObjectIntParameter(self.SpotlightHandle, 8000, 1, self.Client.simxServiceCall())  #可以设置
        self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8001, 10, self.Client.simxServiceCall())  #可以设置
        self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8002, 85/180*3.14159, self.Client.simxServiceCall())  #可以设置
        #self.call_vrep_script_function(0.1, 0, 0.3)
        # casts_shadows = self.Client.simxGetObjectIntParameter(self.SpotlightHandle, 8000,
        #                                                       self.Client.simxServiceCall())   #可以读取
        spot_exponent = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8001,
                                                                self.Client.simxServiceCall())   #可以读取
        spot_cutoff = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8002, self.Client.simxServiceCall())  #可以读取
        constant_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8003,
                                                                              self.Client.simxServiceCall()) #可以读取
        linear_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8004,
                                                                            self.Client.simxServiceCall())   #可以读取
        quadratic_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8005,
                                                                               self.Client.simxServiceCall())  #可以读取
        # print("Casts_shadows:", casts_shadows[1])
        print("Spot_exponent:", spot_exponent[1])
        print("Spot_cutoff:", spot_cutoff[1]*180/3.14159)
        print("Constant_attenuation_factor:", constant_attenuation_factor[1])
        print("Linear_attenuation_factor:", linear_attenuation_factor[1])
        print("Quadratic_attenuation_factor:", quadratic_attenuation_factor[1])
        time.sleep(1)

    def select_light_B(self):
        print("选择光源B")
        # self.Client.simxSetObjectIntParameter(self.SpotlightHandle, 8000, 1, self.Client.simxServiceCall())
        self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8001, 6, self.Client.simxServiceCall())
        self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8002, 80/180*3.14159, self.Client.simxServiceCall())
        #self.call_vrep_script_function(0.2, 0, 0.8)
        # self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8003, 1, self.Client.simxServiceCall())
        # self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8004, 0, self.Client.simxServiceCall())
        # self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8005, 0.01, self.Client.simxServiceCall())

        # casts_shadows = self.Client.simxGetObjectIntParameter(self.SpotlightHandle, 8000,
        #                                                       self.Client.simxServiceCall())
        spot_exponent = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8001,
                                                                self.Client.simxServiceCall())
        spot_cutoff = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8002, self.Client.simxServiceCall())
        constant_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8003,
                                                                              self.Client.simxServiceCall())
        linear_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8004,
                                                                            self.Client.simxServiceCall())
        quadratic_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8005,
                                                                               self.Client.simxServiceCall())
        # print("Casts_shadows:", casts_shadows[1])
        print("Spot_exponent:", spot_exponent[1])
        print("Spot_cutoff:", spot_cutoff[1])
        print("Constant_attenuation_factor:", constant_attenuation_factor[1])
        print("Linear_attenuation_factor:", linear_attenuation_factor[1])
        print("Quadratic_attenuation_factor:", quadratic_attenuation_factor[1])
        time.sleep(1)

    def select_light_C(self):
        print("选择光源C")
        # self.Client.simxSetObjectIntParameter(self.SpotlightHandle, 8000, 1, self.Client.simxServiceCall())
        self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8001, 64, self.Client.simxServiceCall())
        self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8002, 30/180*3.14159, self.Client.simxServiceCall())
        #self.call_vrep_script_function(0.2, 0, 0.8)
        # self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8003, 0.2, self.Client.simxServiceCall())
        # self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8004, 0.5, self.Client.simxServiceCall())
        # self.Client.simxSetObjectFloatParameter(self.SpotlightHandle, 8005, 0.01, self.Client.simxServiceCall())

        # casts_shadows = self.Client.simxGetObjectIntParameter(self.SpotlightHandle, 8000,
        #                                                       self.Client.simxServiceCall())
        spot_exponent = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8001,
                                                                self.Client.simxServiceCall())
        spot_cutoff = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8002, self.Client.simxServiceCall())
        constant_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8003,
                                                                              self.Client.simxServiceCall())
        linear_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8004,
                                                                            self.Client.simxServiceCall())
        quadratic_attenuation_factor = self.Client.simxGetObjectFloatParameter(self.SpotlightHandle, 8005,
                                                                               self.Client.simxServiceCall())
        # print("Casts_shadows:", casts_shadows[1])
        print("Spot_exponent:", spot_exponent[1])
        print("Spot_cutoff:", spot_cutoff[1])
        print("Constant_attenuation_factor:", constant_attenuation_factor[1])
        print("Linear_attenuation_factor:", linear_attenuation_factor[1])
        print("Quadratic_attenuation_factor:", quadratic_attenuation_factor[1])
        time.sleep(1)

    def select_light(self, option):
        if option == 'A':
            self.select_light_A()
        elif option == 'B':
            self.select_light_B()
        elif option == 'C':
            self.select_light_C()
        else:
            print("无效的选项")

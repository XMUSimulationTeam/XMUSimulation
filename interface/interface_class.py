import time
import numpy as np
import cv2
from PIL import Image

class interface_class:

    # 功能：类中赋值
    def __init__(self, client, topic):
        self.client = client
        self.topic = topic

    # 功能：调用CoppeliaSim内部的脚本函数
    # 参数形式：list CallScriptFunction(string FuncName, string ObjName, string scriptType, anyType funcArgs)
    # FuncName(string)：脚本函数名称
    # ObjName(string)：脚本对象名称
    # scriptType(string)：脚本类型
    # funcArgs(anyType)：传递脚本参数
    #
    # 返回参数itemlist中
    # item1(bool): 函数在服务器端是否被成功调用
    # item2(?)：被调用函数的返回值列表
    def CallScriptFunction(self, FuncName, ObjName, scriptType, funcArgs):
        itemlist = self.client.simxCallScriptFunction(FuncName+'@'+ObjName, scriptType, funcArgs, self.topic)
        return itemlist

    # 功能：检索对象参数
    # 参数形式：list GetObjectParameter(string ObjName, number/string parameterID)
    # ObjName(string)：对象名称
    # parameterID(number/string)：待检索的参数的标识符
    # paraType(string)：参数类型
    #
    # 返回参数itemlist中
    # item1 (bool)：函数在服务器端是否被成功调用
    # item2 (number)：检索到的参数
    def GetObjectParameter(self, ObjName, parameterID, paraType):
        ObjHandle = self.client.simxGetObjectHandle(ObjName, self.topic)
        if paraType == 'float':
            itemlist = self.client.simxGetObjectFloatParameter(ObjHandle[1], parameterID, self.topic)
        elif paraType == 'int':
            itemlist = self.client.simxGetObjectIntParameter(ObjHandle[1], parameterID, self.topic)
        elif paraType == 'string':
            itemlist = self.client.simxGetObjectStringParameter(ObjHandle[1], parameterID, self.topic)
        else:
            itemlist = 'please choose float、int or string'
        return itemlist

    # 功能：设置对象参数
    # 参数形式：list SetObjectParameter(string ObjName, number/string parameterID, string parameter, string paraType)
    # ObjName(string)：对象名称
    # parameterID(number/string)：待检索的参数的标识符
    # parameter(paraType)：设置参数
    # paraType(string)：参数类型
    #
    # 返回参数itemlist中
    # item1 (bool)：函数在服务器端是否被成功调用
    # Item2 (number)：错误时为-1，不能设置时为0，成功设置时为1
    def SetObjectParameter(self, ObjName, parameterID, parameter, paraType):
        ObjHandle = self.client.simxGetObjectHandle(ObjName, self.topic)
        if paraType == 'float':
            itemlist = self.client.simxSetObjectFloatParameter(ObjHandle[1], parameterID, parameter, self.topic)
        elif paraType == 'int':
            itemlist = self.client.simxSetObjectIntParameter(ObjHandle[1], parameterID, parameter, self.topic)
        elif paraType == 'string':
            itemlist = self.client.simxSetObjectStringParameter(ObjHandle[1], parameterID, parameter, self.topic)
        else:
            itemlist = 'please choose float、int or string'
        return itemlist

    # 功能：获取仿真图像
    # 参数形式：void GetVisionSensorImage(string ObjName, string ImgType1, string ImgType2)
    # ObjName(string)：对象名称
    # ImgType1(string)：图像类型，分为 color or grey scale
    # ImgType2(string)：图像类型，分为 rgb or depth
    #
    # 显示获取的仿真图片
    def simulationStepStarted(self,msg):
        simTime = msg[1][b'simulationTime']

    def simulationStepDone(self, msg):
        simTime = msg[1][b'simulationTime']
        self.client.doNextStep = True

    def GetVisionSensorImage(self, ObjName, ImgType1, ImgType2):
        self.client.doNextStep = True

        self.client.simxSynchronous(False)
        self.client.simxGetSimulationStepStarted(self.client.simxDefaultSubscriber(self.simulationStepStarted))
        self.client.simxGetSimulationStepDone(self.client.simxDefaultSubscriber(self.simulationStepDone))
        self.client.simxStartSimulation(self.client.simxDefaultPublisher())  # 开始仿真
        startTime = time.time()

        ret, SensorHandle = self.client.simxGetObjectHandle(ObjName, self.topic)

        while time.time() < startTime + 1000:  # 仿真时间设定
            if self.client.doNextStep:
                self.client.doNextStep = False
                '''控制代码'''

                if ImgType1 == 'color':
                    ret1, resolution_color, color_image = self.client.simxGetVisionSensorImage(SensorHandle, False,
                                                                                               self.topic)
                elif ImgType1 == 'grey':
                    ret1, resolution_color, color_image = self.client.simxGetVisionSensorImage(SensorHandle, True,
                                                                                               self.topic)
                else:
                    return 'please choose color or grey'

                if ImgType2 == 'rgb':
                    if ret1:
                        sensor_colorImage = np.frombuffer(color_image, dtype=np.uint8)
                        height_color, width_color = resolution_color[0], resolution_color[1]
                        if ImgType1 == 'color':
                            sensor_colorImage = sensor_colorImage.reshape((height_color, width_color, 3))
                        elif ImgType1 == 'grey':
                            sensor_colorImage = sensor_colorImage.reshape((height_color, width_color, 1))
                        flipud_colorImage = np.flipud(sensor_colorImage)
                        cv2.imshow("sensor_rgbImage", flipud_colorImage)

                elif ImgType2 == 'depth':
                    ret2, resolution_grey, grey_image = self.client.simxGetVisionSensorDepthBuffer(SensorHandle, True,
                                                                                                   True, self.topic)
                    if ret1 and ret2:
                        height_grey, width_grey = resolution_color[0], resolution_color[1]
                        buf = Image.frombytes(mode="F", size=(height_grey, width_grey), data=grey_image,
                                              decoder_name="raw")
                        sensor_greyImage = np.asarray(buf)
                        max_value = np.max(sensor_greyImage)
                        min_value = np.min(sensor_greyImage)
                        sensor_greyImage = (sensor_greyImage - min_value) / (max_value + 1e-9 - min_value)
                        flipud_greyImage = np.flipud(sensor_greyImage)
                        cv2.imshow("sensor_depthImage", flipud_greyImage)

                else:
                    return 'please choose rgb or depth'

                cv2.waitKey(1)

                # client.simxSynchronousTrigger()
            self.client.simxSpinOnce()
        self.client.simxStopSimulation(self.client.simxDefaultPublisher())  # 结束仿真
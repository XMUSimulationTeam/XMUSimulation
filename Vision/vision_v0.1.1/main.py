import b0RemoteApi
import time
import numpy as np
import selectlens
import selectcamera
import selectlight
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import getVisionSensorImage

class ImageBuffer:
    def __init__(self):
        self.buffer = []

    def add_image(self, image):
        self.buffer.append(image)

    def get_latest_image(self):
        if len(self.buffer) > 0:
            return self.buffer[-1]
        else:
            return None

class ImageProcessor(QThread):
    processedImage = pyqtSignal(np.ndarray, np.ndarray)
    stop_signal = pyqtSignal()

    def __init__(self, lighttype, lenstype, cameratype):
        super().__init__()
        self.lightType = lighttype
        self.lensType = lenstype
        self.cameraType = cameratype

    def run(self):
        while True:
            with b0RemoteApi.RemoteApiClient('b0RemoteApi_V-REP', 'b0RemoteApi') as client:
                client.doNextStep = True

                def simulationstepstarted(msg):
                    simTime = msg[1][b'simulationTime']

                def simulationstepdone(msg):
                    simTime = msg[1][b'simulationTime']
                    client.doNextStep = True

                client.simxSynchronous(False)
                client.simxGetSimulationStepStarted(client.simxDefaultSubscriber(simulationstepstarted))
                client.simxGetSimulationStepDone(client.simxDefaultSubscriber(simulationstepdone))
                client.simxStartSimulation(client.simxDefaultPublisher())  # 开始仿真
                startTime = time.time()
                res1, SensorHandle = client.simxGetObjectHandle('Vision_sensor', client.simxServiceCall())  # 获取镜头句柄
                res2, SpotlightHandle = client.simxGetObjectHandle('Spotlight', client.simxServiceCall())  # 获取光源句柄
                light_selector = selectlight.FunctionLightSelector(client, SpotlightHandle)  # 创建选择光源的类对象
                light_selector.select_light(self.lightType)  # 选择光源
                lens_selector = selectlens.FunctionLensSelector(client, SensorHandle)  # 创建选择镜头的类对象
                lens_selector.select_lens(self.lensType)  # 选择镜头
                camera_selector = selectcamera.FunctionCameraSelector(client, SensorHandle)  # 创建选择相机的类对象
                camera_selector.select_camera(self.cameraType)  # 选择相机

                while time.time() < startTime + 1000:
                    if client.doNextStep:
                        client.doNextStep = False
                        '''控制代码'''

                        getImageFunc = getVisionSensorImage.GetVisionSensorImage(client, SensorHandle)  # 创建获取图象的类对象
                        flipud_greyImage, flipud_depthImage = getImageFunc.getimage()  # 获取图像并显示
                        self.processedImage.emit(flipud_greyImage, flipud_depthImage)

                    client.simxSpinOnce()
                client.simxStopSimulation(client.simxDefaultPublisher())  # 结束仿真

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()
        self.image_buffer = ImageBuffer()

    def _init_ui(self):
        self.ui = uic.loadUi("./test.ui")
        self.s1 = self.ui.s1
        self.s1.setRange(0, 20)
        self.s1.setValue(10)
        self.s1.setTickInterval(1)
        self.image_box1 = self.ui.image_box1
        self.image_box2 = self.ui.image_box2
        self.lensFrame = self.ui.lensFrame
        self.cameraFrame = self.ui.cameraFrame
        self.lightFrame = self.ui.lightFrame
        self.start_btn = self.ui.startButton
        self.start_btn.clicked.connect(self.getimage)

    def getimage(self):
        lightType = self.lightFrame.currentText()
        lensType = self.lensFrame.currentText()
        cameraType = self.cameraFrame.currentText()
        self.thread = ImageProcessor(lightType, lensType, cameraType)
        self.thread.processedImage.connect(self.update_image)
        self.thread.start()

    def update_image(self, img1, img2):
        qImage1 = QImage(img1.data.tobytes(), img1.shape[1], img1.shape[0], QImage.Format_Grayscale8)
        pixmap1 = QPixmap.fromImage(qImage1)
        self.image_box1.setPixmap(pixmap1)
        img2 = (img2 * 255).astype(np.uint8)
        qImage2 = QImage(img2.data.tobytes(), img2.shape[1], img2.shape[0], QImage.Format_Grayscale8)
        pixmap2 = QPixmap.fromImage(qImage2)
        self.image_box2.setPixmap(pixmap2)

if __name__=='__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.ui.show()
    app.exec_()



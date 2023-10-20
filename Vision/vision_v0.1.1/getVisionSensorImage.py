import numpy as np
import cv2
from PIL import Image




class GetVisionSensorImage:
    def __init__(self, client, sensor_handle):
        self.Client = client
        self.SensorHandle = sensor_handle

    def getimage(self):
        res1, resolution_grey, grey_image = self.Client.simxGetVisionSensorImage(self.SensorHandle, True,
                                                                                 self.Client.simxServiceCall())
        res2, resolution_depth, depth_image = self.Client.simxGetVisionSensorDepthBuffer(self.SensorHandle, True, True, self.Client.simxServiceCall())

        if res1 and res2:
            sensor_greyImage = np.frombuffer(grey_image, dtype=np.uint8)
            height_grey, width_grey = resolution_grey[0], resolution_grey[1]
            sensor_greyImage = sensor_greyImage.reshape((height_grey, width_grey, 1))
            flipud_greyImage = np.flipud(sensor_greyImage)
            #print(resolution_depth)
            buf = Image.frombytes(mode="F", size=(height_grey, height_grey), data=depth_image, decoder_name="raw")
            #print(len(depth_image))
            sensor_depthImage = np.asarray(buf)
            #print(sensor_depthImage.shape)
            max_value = np.max(sensor_depthImage)
            min_value = np.min(sensor_depthImage)
            sensor_depthImage = (sensor_depthImage - min_value) / (max_value + 1e-9 - min_value)
            flipud_depthImage = np.flipud(sensor_depthImage)

            # cv2.imshow("sensor_greyImage", flipud_greyImage)
            # cv2.imshow("sensor_depthImage", flipud_depthImage)
            # cv2.waitKey(1)

        return (flipud_greyImage,flipud_depthImage)

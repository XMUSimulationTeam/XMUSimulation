import b0RemoteApi
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation


class DataPicture:
    def __init__(self, Client, object_handle, startTime):
        self.client = Client
        self.ObjectHandle = object_handle
        self.StartTime = startTime

        # 设置Matplotlib的交互模式
        plt.ion()

    '''折线图子模块'''
    # 折线图初始化
    def create_line(self):
        # 创建图形和坐标轴
        self.fig, self.ax = plt.subplots(num='line')

        # 创建空列表以存储数据，time_data为横坐标，其它为纵坐标
        self.time_data = []
        self.object_data = []

        self.line, = self.ax.plot([], [], label='data')

        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Data')
        self.ax.legend()

    # 更新折线图数据
    def update_plot_line(self, time_value, object_value):
        # 将新数据添加到列表中
        self.time_data.append(time_value)
        self.object_data.append(object_value)

        # 更新图形
        self.line.set_data(self.time_data, self.object_data)
        self.ax.relim()  # 重新计算坐标轴范围
        self.ax.autoscale_view()  # 自动调整视图范围
        self.fig.canvas.draw()  # 重新绘制图形
        self.fig.canvas.flush_events()  # 刷新GUI事件

    # 更新图像显示
    def update_plot_wrapper_line(self, *args):
        if self.client.doNextStep:  # 如果允许进行下一步仿真
            self.client.doNextStep = False

            # 获取物体的位置信息
            _, position = self.client.simxGetObjectPosition(self.ObjectHandle, -1, self.client.simxServiceCall())

            # 更新图形
            current_time = time.time() - self.StartTime
            self.update_plot_line(current_time, position[0])

            # 执行一次仿真步骤
            self.client.simxSpinOnce()

    '''柱状图子模块'''
    # 柱状图初始化
    def create_bar(self):
        # 创建图形和坐标轴
        self.fig, self.ax = plt.subplots(num='bar')

        # 创建空列表以存储数据，time_data为横坐标，其它为纵坐标
        self.time_data = [1, 2, 3]
        self.object_data1 = 0
        self.object_data2 = 0
        self.object_data3 = 0

        self.bar_container1 = self.ax.bar([], [], label='Data 1')
        self.bar_container2 = self.ax.bar([], [], label='Data 2')
        self.bar_container3 = self.ax.bar([], [], label='Data 3')

        self.ax.set_title('Plot')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Data')
        self.ax.legend()

    # 更新柱状图数据
    def update_plot_bar(self, time_value, object_value1, object_value2,  object_value3):
        # 清空数据
        self.ax.cla()

        # 将新数据添加到列表中
        self.time_data.append(time_value)
        self.object_data1 = object_value1
        self.object_data2 = object_value2
        self.object_data3 = object_value3

        # # 更新柱状图
        # plt.bar(1, self.object_data1, label='X')
        # plt.bar(2, self.object_data2, label='Y')
        # plt.bar(3, self.object_data3, label='Z')

        # 更新柱状图
        self.bar_container1 = self.ax.bar(1, self.object_data1, label='Data 1')
        self.bar_container2 = self.ax.bar(2, self.object_data2, label='Data 2')
        self.bar_container3 = self.ax.bar(3, self.object_data3, label='Data 3')

        # 设置横坐标刻度
        self.ax.set_xticks(range(len(self.time_data)))
        self.ax.set_xticklabels(self.time_data)

        # 重新计算坐标轴范围
        self.ax.relim()
        self.ax.autoscale_view()

        # 重新绘制图形
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    # 更新图像显示
    def update_plot_wrapper_bar(self, *args):
        if self.client.doNextStep:
            self.client.doNextStep = False

            # 获取物体的位置信息
            _, position = self.client.simxGetObjectPosition(self.ObjectHandle, -1, self.client.simxServiceCall())

            # 更新图形
            current_time = time.time() - self.StartTime
            self.update_plot_bar(current_time, position[0], position[1], position[2])

            # print(position[0])
            # 执行一次仿真步骤
            self.client.simxSpinOnce()

    '''饼图子模块'''
    # 饼图初始化
    def create_pie(self):
        # 创建图形和坐标轴
        self.fig, self.ax = plt.subplots(num='pie')

        # 创建空列表以存储数据
        self.labels = ['X', 'Y', 'Z']
        self.sizes = [1, 2, 3]
        self.colors = ['red', 'blue', 'green']

        # 创建饼图
        self.pie_container = self.ax.pie(self.sizes, labels=self.labels, colors=self.colors)

    # 更新饼图数据
    def update_plot_pie(self, object_value1, object_value2, object_value3):
        # 清空数据
        self.ax.cla()

        # 更新数据
        self.sizes[0] = abs(object_value1)
        self.sizes[1] = abs(object_value2)
        self.sizes[2] = abs(object_value3)

        # 更新饼图
        self.pie_container = self.ax.pie(self.sizes, labels=self.labels, colors=self.colors)

        # 重新绘制图形
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    # 更新图像显示
    def update_plot_wrapper_pie(self, *args):
        if self.client.doNextStep:
            self.client.doNextStep = False

            # 获取物体的位置信息
            _, position = self.client.simxGetObjectPosition(self.ObjectHandle, -1, self.client.simxServiceCall())

            # 更新图形
            self.update_plot_pie(position[0], position[1], position[2])

            # 执行一次仿真步骤
            self.client.simxSpinOnce()


    '''热力图子模块'''
    # 创建热力图
    def create_heatmap(self):
        # 读取数据，也可以通过外部csv/xlsx文件进行数据导入
        self.data = np.random.rand(7, 7)

        # 设置坐标轴显示
        self.x_ticks = ["0", "1", "2", "3", "4", "5", "6"]
        self.y_ticks = ["0", "1", "2", "3", "4", "5", "6"]

        # 创建图形和坐标轴
        self.fig, self.ax = plt.subplots(num='heatmap')

        # 创建热力图
        self.heatmap = self.ax.imshow(self.data, cmap='hot', interpolation='nearest')

        # 设置横纵坐标刻度
        self.ax.set_xticks(np.arange(len(self.x_ticks)))
        self.ax.set_yticks(np.arange(len(self.y_ticks)))
        self.ax.set_xticklabels(self.x_ticks)
        self.ax.set_yticklabels(self.y_ticks)

        # 添加颜色标签
        self.fig.colorbar(self.heatmap)

        # 设置标题
        self.ax.set_title('Heatmap')

        # 刷新图形
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    # 更新热力图
    def update_plot_heatmap(self):
        # 清空数据
        self.ax.cla()

        # 更新数据
        self.data = np.random.rand(7, 7)

        self.ax.imshow(self.data, cmap='hot', interpolation='nearest')
        # 直接更新热力图数据

        # 重新绘制图形
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    # 更新图像显示
    def update_plot_wrapper_heatmap(self, *args):
        if self.client.doNextStep:
            self.client.doNextStep = False

            # 获取物体的位置信息
            _, position = self.client.simxGetObjectPosition(self.ObjectHandle, -1, self.client.simxServiceCall())

            # 更新图形
            self.update_plot_heatmap()

            # 执行一次仿真步骤
            self.client.simxSpinOnce()
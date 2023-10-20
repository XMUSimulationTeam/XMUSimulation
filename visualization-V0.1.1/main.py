import b0RemoteApi
import time
import cv2
import numpy as np
import draw
import matplotlib.pyplot as plt
import threading
from matplotlib.animation import FuncAnimation
import tkinter as tk


def main():
    with b0RemoteApi.RemoteApiClient('b0RemoteApi_V-REP', 'b0RemoteApi') as client:
        client.doNextStep = True # 客户端变量，用于控制仿真步骤

        def simulationStepStarted(msg):
            simTime = msg[1][b'simulationTime']  # 仿真步骤开始时的仿真时间

        def simulationStepDone(msg):
            simTime = msg[1][b'simulationTime']  # 仿真步骤完成时的仿真时间
            client.doNextStep = True

        '''基础设置'''
        client.simxSynchronous(False)  # 设置仿真为异步模式
        client.simxGetSimulationStepStarted(client.simxDefaultSubscriber(simulationStepStarted))  # 注册仿真步骤开始的回调函数
        client.simxGetSimulationStepDone(client.simxDefaultSubscriber(simulationStepDone))  # 注册仿真步骤完成的回调函数
        client.simxStartSimulation(client.simxDefaultPublisher())  # 开始仿真
        startTime = time.time()

        '''获取数据对象'''
        # 获取机器人身体的句柄
        _, BodyHandle = client.simxGetObjectHandle('_asti_body', client.simxServiceCall())

        '''可视化部分'''
        # 初始化可视化对象
        module_line = draw.DataPicture(client, BodyHandle, startTime)
        # 初始化折线图模块
        module_line.create_line()
        # 使用FuncAnimation创建动画，实时更新折线图
        ani1 = FuncAnimation(module_line.fig, module_line.update_plot_wrapper_line, interval=100, save_count=10)

        # 初始化可视化对象
        module_bar = draw.DataPicture(client, BodyHandle, startTime)
        # 初始化柱状图模块
        module_bar.create_bar()
        # 使用FuncAnimation创建动画，实时更新柱状图
        ani2 = FuncAnimation(module_bar.fig, module_bar.update_plot_wrapper_bar, interval=100, save_count=10)

        # 初始化可视化对象
        module_pie = draw.DataPicture(client, BodyHandle, startTime)
        # 初始化饼图模块
        module_pie.create_pie()
        # 使用FuncAnimation创建动画，实时更新饼图
        ani3 = FuncAnimation(module_pie.fig, module_pie.update_plot_wrapper_pie, interval=100, save_count=10)

        # 初始化可视化对象
        module_heatmap = draw.DataPicture(client, BodyHandle, startTime)
        # 初始化热力图模块
        module_heatmap.create_heatmap()
        # 使用FuncAnimation创建动画，实时更新热力图
        ani4 = FuncAnimation(module_heatmap.fig, module_heatmap.update_plot_wrapper_heatmap, interval=100, save_count=10, frames=None)

        '''线程部分'''
        # # 创建画图线程
        # plot_thread = threading.Thread(target=lambda: plt.show(block=False))
        # plot_thread.start()

        plt.show(block=False)
        # 运行Tkinter的主事件循环
        tk.mainloop()

        # 结束仿真
        client.simxStopSimulation(client.simxDefaultPublisher())

if __name__ == '__main__':
    main()
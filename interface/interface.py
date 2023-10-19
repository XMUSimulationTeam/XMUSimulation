from environment import b0RemoteApi
import interface_class

with b0RemoteApi.RemoteApiClient('b0RemoteApi_V-REP', 'b0RemoteApi', 60) as client:

    # 定义远程API运作方式为阻塞模式
    topic = client.simxServiceCall()
    # 初始化接口类，用于调用在接口类中的函数
    interface_class = interface_class.interface_class(client, topic)

    # 调用CallScriptFunction函数
    # args = [1, -1, -1, 1]
    # itemlist = interface_class.CallScriptFunction('myFunctionName', 'Robotnik_Summit_XL', 'sim.scripttype_childscript', args)
    # print(itemlist)

    # 调用GetObjectParameter函数
    # itemlist = interface_class.GetObjectParameter('joint_front_left_wheel', 2012, 'float')
    # print(itemlist)

    # 调用SetObjectParameter函数
    # itemlist = interface_class.SetObjectParameter('Vision_sensor', 1001, 2, 'float')
    # print(itemlist)

    # 调用GetVisionSensorImage函数
    # itemlist = interface_class.GetVisionSensorImage('Vision_sensor', 'grey', 'rgb')
    # print(itemlist)
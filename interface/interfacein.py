from environment import b0RemoteApi

with b0RemoteApi.RemoteApiClient('b0RemoteApi_V-REP', 'b0RemoteApi', 60) as client:

    # 定义远程API运作方式为阻塞模式
    topic = client.simxServiceCall()

    # 直接定义函数，用于调用CoppeliaSim内部的脚本函数
    def CallScriptFunction(FuncName, ObjName, scriptType, funcArgs):
        ret = client.simxCallScriptFunction(FuncName+'@'+ObjName, scriptType, funcArgs, topic)
        return ret

    # 调用上面函数
    args = [1, -1, -1, 1]
    # ret = client.simxCallScriptFunction('myFunctionName@Robotnik_Summit_XL', 'sim.scripttype_childscript', args, client.simxServiceCall())
    ret = CallScriptFunction('myFunctionName', 'Robotnik_Summit_XL', 'sim.scripttype_childscript', args)
    print(ret)
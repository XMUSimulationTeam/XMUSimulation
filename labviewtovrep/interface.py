import sim

def ab(a, b):
    sim.simxFinish(-1)
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:
        sim.simxStartSimulation(clientID, sim.simx_opmode_blocking)

        inputInts = [1, -1, -1, 1]
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        inputBuffer.append(78)
        inputBuffer.append(42)
        res, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(clientID, 'Robotnik_Summit_XL',
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'myFunctionName', inputInts,
                                                                                    inputFloats, inputStrings,
                                                                                    inputBuffer,
                                                                                    sim.simx_opmode_blocking)
        if res == sim.simx_return_ok:
            print(res)
            print(retInts)
            print(retFloats)
            print(retStrings)
            print(retBuffer)
            return 'Hello CoppeliaSim!'
        else:
            return 'Remote function call failed'


        # sim.simxStopSimulation(clientID, sim.simx_opmode_blocking)
        # sim.simxFinish(clientID)
    else:
        return 'Failed connecting to remote API server'

c = ab('abbb', 'bccc')
print(c)
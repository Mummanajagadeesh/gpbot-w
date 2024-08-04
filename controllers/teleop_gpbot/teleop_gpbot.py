from controller import Robot, DistanceSensor, Motor, Keyboard
TIME_STEP = 64


robot = Robot()


kb = Keyboard()
kb.enable(TIME_STEP)


ds = []
dsNames = ['ds_right', 'ds_left']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)


wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
leftSpeed = 0.0
rightSpeed = 0.0

while robot.step(TIME_STEP) != -1:
    key = kb.getKey()
    
    if key == Keyboard.UP:
        leftSpeed = 1.0
        rightSpeed = 1.0
    elif key == Keyboard.DOWN:
        leftSpeed = -1.0
        rightSpeed = -1.0
    elif key == Keyboard.RIGHT:
        leftSpeed = 1.0
        rightSpeed = -1.0
    elif key == Keyboard.LEFT:
        leftSpeed = -1.0
        rightSpeed = 1.0
    else:
        leftSpeed = 0.0
        rightSpeed = 0.0

    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)



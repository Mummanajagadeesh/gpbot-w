from controller import Robot, Keyboard

TIME_STEP = 64

def main():
    robot = Robot()
    kb = Keyboard()
    
    ds = []
    dsNames = ['ds_right', 'ds_left']
    for name in dsNames:
        sensor = robot.getDevice(name)
        sensor.enable(TIME_STEP)
        ds.append(sensor)
    
    gp = robot.getDevice('global')
    gp.enable(TIME_STEP)
    
    iu = robot.getDevice('imu')
    iu.enable(TIME_STEP)
    
    wheels = []
    wheels_names = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
    for name in wheels_names:
        wheel = robot.getDevice(name)
        wheel.setPosition(float('inf'))
        wheel.setVelocity(0.0)
        wheels.append(wheel)
    
    kb.enable(TIME_STEP)
    
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
        
        print(f"{ds[0].getValue()} = Right Sensor")
        print(f"{ds[1].getValue()} = Left Sensor")
        
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(rightSpeed)
        wheels[2].setVelocity(leftSpeed)
        wheels[3].setVelocity(rightSpeed)
        
        print(f"X : {gp.getValues()[0]}")
        print(f"Y : {gp.getValues()[1]}")
        print(f"Z : {gp.getValues()[2]}")
        print("########################")
        print(f"Angle X : {iu.getRollPitchYaw()[0]}")
        print(f"Angle Y : {iu.getRollPitchYaw()[1]}")
        print(f"Angle Z : {iu.getRollPitchYaw()[2]}")

if __name__ == "__main__":
    main()

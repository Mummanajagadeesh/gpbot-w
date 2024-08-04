from controller import Robot, Keyboard, DistanceSensor, Motor, Camera, GPS, InertialUnit

TIME_STEP = 64

robot = Robot()
kb = Keyboard()
ds = [robot.getDevice("ds_right"), robot.getDevice("ds_left")]

for sensor in ds:
    sensor.enable(TIME_STEP)

lr = robot.getDevice("linear")
rm = robot.getDevice("RM")

cm = robot.getDevice("CAM")
cm.enable(TIME_STEP)
cm.recognitionEnable(TIME_STEP)


gp = robot.getDevice("global")
gp.enable(TIME_STEP)

iu = robot.getDevice("imu")
iu.enable(TIME_STEP)

wheels = [robot.getDevice(name) for name in ["wheel1", "wheel2", "wheel3", "wheel4"]]
for wheel in wheels:
    wheel.setPosition(float('inf'))
    wheel.setVelocity(0.0)

kb.enable(TIME_STEP)
leftSpeed = 0.0
rightSpeed = 0.0
linear = 0.0
rotate = 0.0

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

    for wheel in wheels:
        wheel.setVelocity(leftSpeed if wheel in [wheels[0], wheels[2]] else rightSpeed)

    if key == ord('W') and linear < 0.19:
        linear += 0.005
    elif key == ord('S') and linear > 0:
        linear -= 0.005
    lr.setPosition(linear)

    if key == ord('A') and rotate < 1.57:
        rotate += 0.05
    elif key == ord('D') and rotate > -1.57:
        rotate -= 0.05
    rm.setPosition(rotate)

    print("Right Sensor:", ds[0].getValue())
    print("Left Sensor:", ds[1].getValue())
    print("GPS - X:", gp.getValues()[0], "Y:", gp.getValues()[1], "Z:", gp.getValues()[2])
    print("IMU - Roll:", iu.getRollPitchYaw()[0], "Pitch:", iu.getRollPitchYaw()[1], "Yaw:", iu.getRollPitchYaw()[2])

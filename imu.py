import time
from Adafruit_BNO055 import BNO055

# Create and initialize the BNO055 sensor connection
sensor = BNO055.BNO055(busnum=1)

# Check if the sensor is connected properly
if not sensor.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print sensor data
while True:
    temp = sensor.read_temp()
    accel = sensor.read_accelerometer()
    mag = sensor.read_magnetometer()
    gyro = sensor.read_gyroscope()
    euler = sensor.read_euler()
    quaternion = sensor.read_quaternion()
    lin_accel = sensor.read_linear_acceleration()
    gravity = sensor.read_gravity()

    print("Temperature: {} degrees C".format(temp))
    print("Accelerometer (m/s^2): {}".format(accel))
    print("Magnetometer (microteslas): {}".format(mag))
    print("Gyroscope (rad/s): {}".format(gyro))
    print("Euler angle: {}".format(euler))
    print("Quaternion: {}".format(quaternion))
    print("Linear acceleration (m/s^2): {}".format(lin_accel))
    print("Gravity (m/s^2): {}".format(gravity))

    time.sleep(1)

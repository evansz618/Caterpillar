#Enter code

from motorController import *

board = NanoMotorBoard()
def Init():
    print("reboot")
    board.reboot()
    time.sleep_ms(500)
    motors = []

    for i in range(2):
        motors.append(DCMotor(i))
    for motor in motors:
        b = motor.setDuty(0)
        b = motor.resetEncoder(0)

    return motors

motors = Init()

def Stop(motors):
    for motor in motors:
        b = motor.setDuty(0)



from pyfirmata import Arduino,util
import time
import sys
from pymata4 import pymata4

def test_pyFrimata():
    board = Arduino('COM3')
    it = util.Iterator(board)
    it.start()
    pin_3 = board.get_pin('d:3:p')

    # while True:
    #     board.digital[3].write(0)
    #     time.sleep(1)
    #     board.digital[3].write(1)
    #     time.sleep(1)
    while True:
        for i in range(0, 5, 1):
            pin_3.write(i*0.1)
            time.sleep(0.1)
        for i in range(5, 0, 1):
            pin_3.write(i*0.1)
            time.sleep(0.1)

board = pymata4.Pymata4()

def test_pymata_light():
    while True:
        board.digital_write(pin, 1)
        time.sleep(1)
        board.digital_write(pin, 0)
        time.sleep(1)

def test_pymata_servo():
    board.set_pin_mode_servo(pin)
    # set the servo to 0 degrees
    for i in range(0, 5):
        board.servo_write(pin, 0)
        time.sleep(1)
        # set the servo to 90 degrees
        board.servo_write(pin, 90)
        time.sleep(1)
        # set the servo to 180 degrees
        board.servo_write(pin, 180)

NUM_STEPS = 512
STEPPER_PINS = [8, 9, 10, 11]
# NOTE: Single stepper only. Multiple steppers not supported.
def test_pymata_stepper():
    board.set_pin_mode_stepper(NUM_STEPS, STEPPER_PINS)
    while True:
        board.stepper_write(50, 500)
        time.sleep(1)
        board.stepper_write(50, -500)
        time.sleep(1)

def clockwise():
    for i in range(4):
        for j in range(4):
            if j == i:
                board.digital_write(STEPPER_PINS[j], 1)
            else:
                board.digital_write(STEPPER_PINS[j], 0)
        time.sleep(.0005)

def anticlock():
    for i in range(4, 0, -1):
        for j in range(4):
            if j == i:
                board.digital_write(STEPPER_PINS[j], 1)
            else:
                board.digital_write(STEPPER_PINS[j], 0)
        time.sleep(.0005)


def stepper():
    for i in STEPPER_PINS:
        board.set_pin_mode_digital_output(i)
    while True:
        for i in range(0, 100):
            clockwise()
        for i in range(0, 100):
            anticlock()

def play_tone():
    TONE_PIN = 4
    board.set_pin_mode_tone(TONE_PIN)
    # specify pin, frequency and duration and play tone
    board.play_tone(TONE_PIN, 1000, 500)
    time.sleep(2)

    # specify pin and frequency and play continuously
    board.play_tone_continuously(TONE_PIN, 2000)
    time.sleep(2)

    # specify pin to turn pin off
    board.play_tone_off(TONE_PIN)

    # clean up
    board.shutdown()

if __name__ == '__main__':
    # test_pymata_stepper()
    # stepper()
    play_tone()
from pyfirmata import Arduino,util
import time
board = Arduino('COM3')
it = util.Iterator(board)
it.start()
# board.analog[3].enable_reporting()
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
import serial
import common
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 9600)

common.wait_for_start(ser)

plt.axis([0, 10000, 0, 1024])

for i in range(10000):
    line = ser.readline()
    y = common.get_value(line)
    print(y)
    plt.plot(i, y)
    plt.pause(0.00001)


plt.show()


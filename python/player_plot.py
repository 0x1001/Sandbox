import serial
import common
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 9600)

common.wait_for_start(ser)

fig = plt.gcf()
fig.show()
fig.canvas.draw()

x = []
y = []
i = 0
while True:
    for _ in range(10):
        line = ser.readline()
        d = common.get_value(line)
        print(d)

        x.append(i)
        y.append(d)
        i += 1

    plt.plot(x, y, 'b')  # plot something

    # update canvas immediately
    plt.xlim([0, 1000])
    plt.ylim([0, 1024])
    # plt.pause(0.01)  # I ain't needed!!!
    fig.canvas.draw()

    if i == 1000:
        i = 0
        x = []
        y = []
        fig.clf()




import matplotlib.pyplot as plt
import random
import time

fig = plt.gcf()
fig.show()
fig.canvas.draw()

x = []
y = []
while True:
    # compute something
    x.append(random.random())
    y.append(random.random())
    plt.plot(x, y)  # plot something

    # update canvas immediately
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    # plt.pause(0.01)  # I ain't needed!!!
    fig.canvas.draw()
    time.sleep(0.05)
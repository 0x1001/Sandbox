import pygame.midi
import time
import serial


ser = serial.Serial("COM3", 9600)

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(20)
last_step = 0

RANGE_MAX = 127.0
RANGE_MIN = 40.0

while True:
    line = ser.readline()
    potentiometer = int(line.decode("utf8").strip())
    step = int((potentiometer - 0.0) * (RANGE_MAX - RANGE_MIN) / (1023.0 - 0.0) + RANGE_MIN)

    if last_step != step:
        player.note_off(last_step, 127)
        player.note_on(step, 127)
        last_step = step
        print(step)

    if potentiometer == 0:
        player.note_off(step, 127)

del player
pygame.midi.quit()
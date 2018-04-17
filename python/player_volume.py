import pygame.midi
import time
import serial
import pygame.mixer


ser = serial.Serial("COM3", 9600)

pygame.mixer.init()
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(20)
last_step = 0

NOTE = 50

RANGE_MAX = 127.0
RANGE_MIN = 40.0

while True:
    line = ser.readline()
    potentiometer = int(line.decode("utf8").strip())
    step = int((potentiometer - 0.0) * (RANGE_MAX - RANGE_MIN) / (1023.0 - 0.0) + RANGE_MIN)

    if last_step != step:
        #player.note_off(NOTE, step)
        player.note_on(NOTE, step)
        last_step = step

    print(potentiometer)

    if potentiometer == 0:
        player.note_off(NOTE, step)

del player
pygame.midi.quit()
pygame.mixer.quit()
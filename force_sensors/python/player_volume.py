import pygame.midi
import time
import serial
import common

ser = serial.Serial("COM3", 9600)

common.wait_for_start(ser)

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(20)
last_value_1 = 0
last_value_2 = 0

NOTE_1 = 50
NOTE_2 = 64

RANGE_MAX = 127.0
RANGE_MIN = 40.0

while True:
    line = ser.readline()

    if common.first_button(line):
        potentiometer = common.get_value(line)
        step = int((potentiometer - 0.0) * (RANGE_MAX - RANGE_MIN) / (1023.0 - 0.0) + RANGE_MIN)

        if last_value_1 != step:
            #player.note_off(NOTE_1, step)
            player.note_on(NOTE_1, step)
            last_value_1 = step

        print(potentiometer)

        if potentiometer == 0:
            player.note_off(NOTE_1, step)

    if common.second_button(line):
        potentiometer = common.get_value(line)
        step = int((potentiometer - 0.0) * (RANGE_MAX - RANGE_MIN) / (1023.0 - 0.0) + RANGE_MIN)

        if last_value_2 != step:
            #player.note_off(NOTE_2, step)
            player.note_on(NOTE_2, step)
            last_value_2 = step

        print(potentiometer)

        if potentiometer == 0:
            player.note_off(NOTE_2, step)

del player
pygame.midi.quit()
pygame.mixer.quit()
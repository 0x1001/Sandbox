import pygame.midi
import time

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

player.note_on(100, 127)
time.sleep(1)
player.note_off(64, 127)

del player
pygame.midi.quit()
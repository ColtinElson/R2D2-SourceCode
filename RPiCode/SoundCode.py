import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('/home/pi/Downloads/R2D2.wav')

pygame.mixer.music.play()

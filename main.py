import pygame
import sys
import os
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 750))

bg = pygame.image.load(os.path.join("./", "Bg.jpg"))
pygame.mouse.set_visible(1)
pygame.display.set_caption('Jogo mt foda do pygame')

running = True
while running:
  clock.tick(60)
  screen.blit(bg, (0,0))
  x,y = pygame.mouse.get_pos()

  pygame.display.update()

  # Did the user click the window close button?
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
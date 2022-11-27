import pygame
import sys
import os
from pygame.locals import *

screenWidth = 1000
screenHeigh = 750

sprite = pygame.image.load("armario.png")
# sprite = pygame.transform.scale(pygame.image.load("armario.png")), (100, 100)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeigh))

bg = pygame.image.load(os.path.join("./", "Bg.jpg"))
pygame.mouse.set_visible(1)
pygame.display.set_caption('Jogo mt foda do pygame')

def frames(self, inputs):
  if inputs[K_UP]:
    self.rect.move_ip(0, -5)
  if inputs[K_DOWN]:
    self.rect.move_ip(0, 5)
  if inputs[K_LEFT]:
    self.rect.move_ip(-5, 0)
  if inputs[K_RIGHT]:
    self.rect.move_ip(5, 0)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = sprite.convert_alpha()
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
    self.rect = self.surf.get_rect()

player = Player()

running = True
while running:
  clock.tick(60)
  screen.blit(bg, (0,0))
  x,y = pygame.mouse.get_pos()
  screen.blit(player.surf, player.rect)

  pygame.display.flip()

  inputs = pygame.key.get_pressed()
  frames(player, inputs)
  if player.rect.left < 0:
    player.rect.left = 0
  if player.rect.right > screenWidth:
    player.rect.right = screenWidth
  if player.rect.top <= 0:
    player.rect.top = 0
  if player.rect.bottom >= screenHeigh:
    player.rect.bottom = screenHeigh


  for event in pygame.event.get():
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        running = False
    elif event.type == QUIT:
      running = False
  
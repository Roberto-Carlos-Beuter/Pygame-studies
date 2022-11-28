import pygame
import sys
import os
from pygame.locals import *
from time import sleep

screenWidth = 1000
screenHeigh = 750

def gravity(self):
 while player.rect.bottom <= 680:
  ie = 2
  ie *= 2
  self.rect.move_ip(0, ie)
  
sprite = pygame.image.load("armario.png")
playerImage = pygame.transform.scale(sprite, (100, 110))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeigh))

bg = pygame.image.load(os.path.join("./", "Bg.jpg"))
pygame.mouse.set_visible(1)
pygame.display.set_caption('Jogo mt foda do pygame')

def frames(self, inputs):
  if inputs[K_UP] or inputs[K_w]:
    self.rect.move_ip(0, -5)
  if inputs[K_DOWN] or inputs[K_s]:
    self.rect.move_ip(0, 5)
  if inputs[K_LEFT] or inputs[K_a]:
    self.rect.move_ip(-5, 0)
  if inputs[K_RIGHT] or inputs[K_d]:
    self.rect.move_ip(5, 0)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = playerImage.convert_alpha()
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
  gravity(player)
  if player.rect.left < 0:
    player.rect.left = 0
  if player.rect.right > screenWidth:
    player.rect.right = screenWidth
  if player.rect.top <= 0:
    player.rect.top = 0
  if player.rect.bottom >= 685:
    player.rect.bottom = 685

  for event in pygame.event.get():
    if event.type == KEYDOWN and event.key == K_ESCAPE:
      running = False
    elif event.type == QUIT:
      running = False
  
import pygame
from pygame.sprite import Group
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int], *groups: Group):
        super().__init__(*groups)
        self.image = pygame.image.load('assets/rock.png')
        self.rect = self.image.get_rect(topleft=pos)

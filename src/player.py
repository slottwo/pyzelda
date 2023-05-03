from typing import Any
import pygame
from pygame.sprite import Group
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,
                 pos: tuple[int],
                 *groups: Group) -> None:
        super().__init__(*groups)
        # self.image = pygame.transform.scale(
        #     pygame.image.load('assets/player.png').convert_alpha(),
        #     (TILE_SIZE*2,)*2)

        self.image = pygame.image.load('assets/player.png')
        
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()

    def input(self):
        # mapa das teclas valoradas com True se pressionadas
        keys = pygame.key.get_pressed()

        # MOVIMENTAÇÃO

        # na tela do computador, o y cresce para baixo
        if keys[pygame.K_UP] & keys[pygame.K_DOWN]:
            self.direction.y = 0
        elif keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] & keys[pygame.K_RIGHT]:
            self.direction.x = 0
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # ATAQUE

        if keys[pygame.K_SPACE]:
            ...

    def update(self, *args: Any, **kwargs: Any):
        self.input()
        self.rect.x += self.direction.x * TILE_SIZE
        self.rect.y += self.direction.y * TILE_SIZE
        super().update(*args, **kwargs)

import pygame
from debug import debug
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self, tile_map: tuple[tuple[str]]):
        # recebe a superfície da tela do jogo
        self.display_surface = pygame.display.get_surface()

        # configura os grupos de sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # carrega os elementos do nível carregando
        self.create_map(tile_map)

    def create_map(self, tile_map: tuple[tuple[str]]):
        # carrega os elementos iniciais do nível
        for row_index, row in enumerate(tile_map):
            for column_index, tile in enumerate(row):
                x = column_index * TILE_SIZE
                y = row_index * TILE_SIZE
                match tile:
                    case 'x':
                        # cria um novo tile salvando-o nos grupos visíveis e obstáculos
                        Tile((x, y), self.visible_sprites,
                             self.obstacles_sprites)
                    case 'p':
                        # cria o player salvando-o nos grupos de sprites visíveis
                        self.player = Player((x, y), self.visible_sprites)

    def clear_map(self):
        self.visible_sprites.clear()
        self.obstacles_sprites.clear()

    def run(self):
        # atualiza e desenha o jogo
        self.player.update()
        self.visible_sprites.draw(self.display_surface)
        debug(self.player.direction)

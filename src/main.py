import pygame
import sys
from settings import *
from level import Level
from pygame.color import Color


class Game:
    def __init__(self) -> None:
        # configuração geral do pygame
        pygame.init()
        pygame.display.set_caption('pyZelda')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()  # "FPS"

        self.level = Level(WORLD_MAP)

    def run(self):
        while True:

            # fechar jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # pinta tela com a cor da grama
            self.screen.fill(color=Color('0x99e550'))

            # atualiza e desenha o jogo
            self.level.run()

            # atualiza a tela para o frame atual
            pygame.display.update()

            # espera 1/FPS segundos a cada frame
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()  # cria o jogo (configurando-o e tudo mais)
    game.run()  # inicia o jogo

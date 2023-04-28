import pygame
import sys
from settings import *


class Game:
    def __init__(self) -> None:

        # configuração geral
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()  # "FPS"

    def run(self):
        while True:

            # fechar jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # pinta tela de preto
            self.screen.fill('black')

            # atualiza o frame atual da tela
            pygame.display.update()

            # espera 1/FPS segundos a cada frame
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()  # cria o jogo (configurando-o e tudo mais)
    game.run()  # inicia o jogo

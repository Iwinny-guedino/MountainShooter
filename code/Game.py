import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # comando obrigatorio para o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # criando tela e definindo seu tamanho

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass



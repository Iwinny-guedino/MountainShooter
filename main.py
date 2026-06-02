import pygame

print('Setup Start')
pygame.init() #comando obrigatorio para o pygame
window = pygame.display.set_mode(size=(600, 480)) #criando tela e definindo seu tamanho
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close Window
            quit() # end pygame

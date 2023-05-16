import pygame

pygame.init()

# Gera tela principal
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption('PYGAME')


game = True

# Loop principal
while game:
    #  Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Gera saídas
    window.fill((229, 35, 151))  # Preenche com a cor rosa

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

pygame.quit()  
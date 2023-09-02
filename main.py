import pygame

WIDTH = 360
HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othellia")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 0, 255))
    pygame.display.flip()

pygame.quit()

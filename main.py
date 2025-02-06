import pygame
from Card import Card
from CardManager import spawn_cards

# Pygame setup
pygame.init()
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Generate cards
cards = spawn_cards(20)

while running:
    screen.fill("grey")  # Clear screen

    for event in pygame.event.get(): # Event managment
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for card in cards:
                    if card.is_clicked(event.pos):
                        card.on_click()

    # Draw all cards
    for card in cards:
        card.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
from CardManager import spawn_cards
from Player import Player
from Enemy import Enemy
from Button import Button

# Pygame setup
pygame.init()
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Create instances of Player and Enemy
player = Player(health=100, level=1)
enemy = Enemy(health=80, level=1)

# Generate cards with same probabilities at start
probabilities = {'F': 1, 'E': 1, 'L': 1, 'W': 1}
cards = spawn_cards(20, player, probabilities)

# Button Click Functions
def button_fire_action():
    player.player_attack(enemy, player.fire)

def button_earth_action():
    player.player_attack(enemy, player.earth)

def button_lightning_action():
    player.player_attack(enemy, player.lightning)

def button_water_action():
    player.player_attack(enemy, player.water)

def reset_button_action():
    print("Extra Button clicked!")

# Elemental buttons positions
button_x = 1000
button_y = 750
button_width = 50
button_height = 50
button_padding = 60


elemental_buttons = [
    Button(button_x, button_y, button_width, button_height, "F", (200, 100, 100), button_fire_action),
    Button(button_x + button_padding, button_y, button_width, button_height, "E", (100, 200, 100), button_earth_action),
    Button(button_x, button_y + button_padding, button_width, button_height, "L", (200, 200, 100), button_lightning_action),
    Button(button_x + button_padding, button_y + button_padding, button_width, button_height, "W", (100, 100, 200), button_water_action),
]

reset_button = Button(1300, 780, 120, 50, "Reset Button", (150, 150, 150), reset_button_action)

while running:
    screen.fill("grey")  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for card in cards:
                    if card.is_clicked(event.pos):
                        card.on_click()

                # Check if buttons are clicked
                for button in elemental_buttons:
                    if button.is_clicked(event.pos):
                        button.handle_click()

                if reset_button.is_clicked(event.pos):
                    reset_button.handle_click()

    # UI Elements
    enemy.draw(screen)  # Enemy Health Bar and Figure (top)
    for card in cards:
        card.draw(screen)  # Cards (middle)
    player.draw(screen)  # Player Health Bar and Figure (bottom)

    # Buttons
    for button in elemental_buttons:
        button.draw(screen)
    reset_button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
from CardManager import spawn_cards, reset_card_used
from Player import Player
from Enemy import Enemy
from Button import Button
from Element import Fire, Earth, Water, Lightning

# Pygame setup
pygame.init()
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Player and Enemy instances
player = Player(health=100, level=1)
enemy = Enemy(health=80, level=1)

# Generate cards
cards = spawn_cards(20, player, player.probabilities)

used_cards = []  # Cards to be removed next turn


def remove_used_cards():
    global cards
    cards = [card for card in cards if card not in used_cards]


selected_element = None
selected_cards = 0
max_card_clicks = player.max_cards_flipped


# Button Click Functions
def reset_button_action():
    global cards, selected_element, selected_cards
    if selected_element is not None:
        return
    print("Reset Button clicked! Ending turn and refreshing cards.")

    # Spawn a new set of 20 cards
    cards = spawn_cards(20, player, player.probabilities)

    # Reset turn variables
    selected_element = None
    selected_cards = 0

    # Enemy's Turn
    enemy_turn()


def select_element(element_type):
    global selected_element, selected_cards
    if element_type == "Fire":
        selected_element = player.fire
    elif element_type == "Earth":
        selected_element = player.earth
    elif element_type == "Water":
        selected_element = player.water
    elif element_type == "Lightning":
        selected_element = player.lightning

    selected_cards = 0  # Reset the card counter
    print(f"Element {element_type} selected!")


def enemy_turn():
    if enemy.skip_turn:
        print("Enemy skips turn because of Zapped")
        enemy.skip_turn = False
        return

    enemy.handle_status_effect(player)
    print("Enemy attacks the player!")
    player.take_damage(5)


# Elemental Buttons
button_x = 1000
button_y = 750
button_width = 50
button_height = 50
button_padding = 60

buttons = [
    Button(button_x, button_y, button_width, button_height, "F", (200, 100, 100), lambda: select_element("Fire")),
    Button(button_x + button_padding, button_y, button_width, button_height, "E", (100, 200, 100),
           lambda: select_element("Earth")),
    Button(button_x, button_y + button_padding, button_width, button_height, "W", (100, 100, 200),
           lambda: select_element("Water")),
    Button(button_x + button_padding, button_y + button_padding, button_width, button_height, "L",
           (200, 200, 100), lambda: select_element("Lightning")),
]

reset_button = Button(1300, 780, 120, 50, "Reset Button", (150, 150, 150), reset_button_action)


def draw_all():
    screen.fill("grey")  # Clear screen
    # Draw UI Elements
    enemy.draw(screen)  # Enemy Health Bar (top)
    for card in cards:
        card.draw(screen)  # Cards (middle)
    player.draw(screen)  # Player Health Bar and Figure

    # Draw buttons
    for button in buttons:
        button.draw(screen)
    reset_button.draw(screen)

    pygame.display.flip()


# Game loop (for now: Select element with button -> Click 2(for now) cards -> Player attack -> Reset)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Reset cards and end turn
                if reset_button.is_clicked(event.pos):
                    reset_button.handle_click()

                # Select an element
                elif selected_element is None:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            button.handle_click()

                # Click cards
                elif selected_cards < max_card_clicks:
                    for card in cards:
                        if card.is_clicked(event.pos):
                            card.on_click()
                            selected_cards += 1

                            # If the clicked card matches the selected element, increase temp_level
                            if (selected_element == player.fire and card.card_type == "F") or \
                                    (selected_element == player.earth and card.card_type == "E") or \
                                    (selected_element == player.water and card.card_type == "W") or \
                                    (selected_element == player.lightning and card.card_type == "L"):
                                selected_element.increase_temp_level()
                                used_cards.append(card)
                                print(f"temp level increased to {selected_element.temp_level}")

                # Attack the enemy after selecting two cards
                if selected_cards == max_card_clicks:
                    # Wait for cards to finish flipping then continue
                    while not all([card.anim_state == 2 or not card.used for card in cards]):
                        draw_all()
                        clock.tick(60)

                    print("Player attacks the enemy!")

                    player.player_attack(enemy, selected_element)

                    # Enemy's Turn
                    enemy_turn()
                    # Reset for next turn
                    selected_element.reset_temp_level()  # Reset temp_level
                    selected_element = None
                    selected_cards = 0
                    # Remove used cards
                    cards = [card for card in cards if card not in used_cards]
                    print(len(cards))
                    used_cards.clear()
                    reset_card_used(cards) # Sets cards.used to False, cards.anim_state and cards.anim_counter to 0

    draw_all()
    clock.tick(60)


pygame.quit()
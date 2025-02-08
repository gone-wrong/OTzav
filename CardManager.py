from Card import Card
import random

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 960


def spawn_cards(ct, player, probabilities):

    cards = []
    card_width = 100
    card_height = 150
    padding = 20
    total_row_width = (10 * card_width) + (9 * padding)
    start_x = (SCREEN_WIDTH - total_row_width) // 2
    start_y = (SCREEN_HEIGHT // 2) - ((ct // 10) * card_height / 2) - 10
    y = start_y

    #Card types by elements
    element_types = {
        "F": (200, 100, 100),  #Fire (Red)
        "E": (100, 200, 100),  #Earth (Green)
        "L": (200, 200, 100),  #Lightning (Yellow)
        "W": (100, 100, 200),  #Water (Blue)
    }


    #Weighted list for random selection
    elements = list(probabilities.keys())
    weights = list(probabilities.values())

    for i in range(ct):
        x = start_x + (i % 10) * (card_width + padding)
        if i % 10 == 0 and i != 0:
            y += card_height + padding

        #Choose card type based on the given probabilities
        card_type = random.choices(elements, weights)[0]
        color = element_types[card_type]

        card = Card(card_type, x, y, color, player)
        cards.append(card)

    return cards

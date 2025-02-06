from Card import Card
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 960

def spawn_cards(ct):
    cards = []
    cards_total = ct
    rows_total = cards_total // 10
    card_width = 100
    card_height = 150
    padding = 20

    total_row_width = (10 * card_width) + (9 * padding)
    start_x = (SCREEN_WIDTH - total_row_width) // 2
    start_y = (SCREEN_HEIGHT // 2) - (card_height * rows_total / 2) - 10
    y = start_y
    for i in range(cards_total):
        x = start_x + (i % 10) * (card_width + padding)
        if i % 10 == 0 and i != 0:
            y += card_height + padding
        card = Card(str(i + 1), x, y)
        cards.append(card)

    return cards
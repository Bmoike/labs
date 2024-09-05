# assigns cards a value in a dictionary
cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
value_of_cards = {i: cards.index(i) + 2 for i in cards}


# checks for a straight
def check_straight(card1, card2, card3):
    values = [value_of_cards[card1], value_of_cards[card2], value_of_cards[card3]]
    sort_cards = sorted(values)

    sequence = False
    for i in range(len(sort_cards) - 1):
        if sort_cards[i] + 1 == sort_cards[i + 1]:
            sequence = True
        else:
            sequence = False

    if sequence:
        return max(sort_cards)
    else:
        return 0


# checks for a 3 of a kind
def check_3ofa_kind(card1, card2, card3):
    if value_of_cards[card1] == value_of_cards[card2] == value_of_cards[card3]:
        return value_of_cards[card1]
    else:
        return 0


# checks for a royal flush
def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0
    pass


def play_cards(left1, left2, left3, right1, right2, right3):
    # check for higher straight win condition
    if check_straight(left1, left2, left3) != 0 and check_straight(right1, right2, right3) != 0:
        if check_straight(left1, left2, left3) == check_straight(right1, right2, right3):
            return 0
        elif check_straight(left1, left2, left3) > check_straight(right1, right2, right3):
            return -1
        else:
            return 1
    # check for higher 3 of a kind win condition
    elif check_3ofa_kind(left1, left2, left3) != 0 and check_3ofa_kind(right1, right2, right3) != 0:
        if check_3ofa_kind(left1, left2, left3) > check_3ofa_kind(right1, right2, right3):
            return -1
        elif check_3ofa_kind(left1, left2, left3) < check_3ofa_kind(right1, right2, right3):
            return 1
        else:
            return 0

    # check for straight vs 3 kind win condition
    elif check_straight(left1, left2, left3) != 0 and check_3ofa_kind(right1, right2, right3) != 0:
        return -1
    elif check_straight(right1, right2, right3) != 0 and check_3ofa_kind(left1, left2, left3):
        return 1

    # check for one player with royal flush and other doesn't
    elif check_royal_flush(left1, left2, left3) != 0 and check_royal_flush(right1, right2, right3) == 0:
        return -1
    elif check_royal_flush(left1, left2, left3) == 0 and check_royal_flush(right1, right2, right3) != 0:
        return -1
    # tie condition
    else:
        return 0

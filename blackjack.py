import p1_random as p1
rng = p1.P1Random()
game_num = -1
card = "0"
wins = 0
losses = 0
ties = 0
player_hand = 0
dealer_hand = 0

def deal():
    global wins, losses, player_hand
    card_num = rng.next_int(13) + 1
    if card_num >=2 and card_num <=10:            #number cards
        card_value = int(card_num)
        card = f"{card_value}"

    if card_num == 1:                #face cards
        card_value = 1
        card = "ACE"

    if card_num == 11:
        card_value = 10
        card = "JACK"

    if card_num == 12:
        card_value = 10
        card = "QUEEN"

    if card_num == 13:
        card_value = 10
        card = "KING"

    print(f"Your card is a {card}!")
    player_hand += int(card_value)
    print(f"Your hand is: {player_hand}")
    if player_hand < 21:
        menu()

    if player_hand == 21:
        print("BLACKJACK! You win!")
        wins += 1
        start()

    if player_hand > 21:
        print("You exceeded 21! You lose.")
        losses += 1
        start()


def menu():
    global wins, losses, ties
    menu_selection = int(input(
        "1. Get another card\n"
        "2. Hold hand\n"
        "3. Print statistics\n"
        "4. Exit\n"
        "Choose an option:"))

    if menu_selection == 1:
        deal()

    elif menu_selection == 2:
        dealer_hand = rng.next_int(11) + 16
        print(f"Dealer's hand: {dealer_hand}")
        print(f"Your hand is: {player_hand}")
        if player_hand == dealer_hand:
            print("It's a tie! No one wins!")
            ties += 1
            start()

        if dealer_hand > 21:
            print("You win!")
            wins += 1
            start()

        if player_hand > dealer_hand:
            print("You win!")
            wins += 1
            start()

        if dealer_hand == 21 or dealer_hand > player_hand:
            print("Dealer wins!")
            losses += 1
            start()

    elif menu_selection == 3:

        print(f"Number of Player wins: {wins}")
        print(f"Number of Dealer wins: {losses}")
        print(f"Number of tie games: {ties}")
        print(f"Total # of games played is: {game_num}")
        print(f"Percentage of Player wins: {round(((wins / game_num) * 100), 2)}%")
        menu()

    elif menu_selection == 4:
        exit()

    else:
        print("Invalid input!\n"
        "Please enter an integer value between 1 and 4.")
        menu()




def start():
    global player_hand, game_num
    game_num += 1
    player_hand = 0
    print(f"START GAME #{game_num + 1}")
    deal()

start()
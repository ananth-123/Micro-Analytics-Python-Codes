import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def show_hands(player_hand, dealer_hand, show_dealer_card=False):
    print(f"\nYour cards: {player_hand}, current score: {calculate_score(player_hand)}")
    if show_dealer_card:
        print(f"Computer's cards: {dealer_hand}, current score: {calculate_score(dealer_hand)}")
    else:
        print(f"Computer's first card: {dealer_hand[0]}")

def blackjack():
    player_hand = []
    dealer_hand = []
    
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        for _ in range(2):
            player_hand.append(deal_card())
            dealer_hand.append(deal_card())
        
        show_hands(player_hand, dealer_hand)

        should_continue = True
        while should_continue:
            if input("\nType 'y' to get another card, type 'n' to pass: ") == "y":
                player_hand.append(deal_card())
                show_hands(player_hand, dealer_hand)
                
                if calculate_score(player_hand) > 21:
                    show_hands(player_hand, dealer_hand, show_dealer_card=True)
                    should_continue = False
            else:
                should_continue = False

        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
        
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        if player_score > 21:
            print("You went bust, you lose!")
        elif dealer_score > 21 or player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("It's a draw.")

if __name__ == "__main__":
    blackjack()

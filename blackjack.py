# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *



# Write all of your part 4 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.


user_hand = draw_starting_hand("YOUR")

while user_hand < 21:

    should_hit = input('You have ' + str(user_hand) + ". Hit (y/n)? ")
    if should_hit == 'n':
        break
    elif should_hit == 'y':
        new_card = draw_card()
        user_hand += new_card
    
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_hand)

dealer_hand = draw_starting_hand("DEALER")

while dealer_hand < 17:
    if dealer_hand < 17:
        print("Dealer has {}.".format(dealer_hand))
    new_card2 = draw_card()
    
    dealer_hand += new_card2
    

print_end_turn_status(dealer_hand)

print_end_game_status(user_hand, dealer_hand)



  

import random

# TODO: Implement the Card class as follows...

# 1) Add the class declaration. Use the following class comment.
class Card:
    """
    Responsibility: to hold and display card information

    Attributes:
    
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self) -> None:
        """ Constructs
    
        Args: 
            self (cards): An instance of cards
        """
        self.value = 0
        # Game starts with 300 points
        self.points = 300

# 3) Angela Display int between 1 to 13
    def display_card(self):
        self.value = random.randint(1, 13)

# 4) Angela Player guess higher or lower
#    def ask_player():
#        pass

# 5) Francisco Display amount earned or lost +100 points if correct, -75 if incorrect
#    def earned_lost():
#        pass

# 6) Franciso Keep overall score, game started at 300, ends if player reaches 0
#    def overall_score():
#        pass

# 7) Dylan Ask playing to keep playing if points > 0
"""
    def keep_playing():
        print('Do you wish to continue play:')
        x = input()
        if x == 'Y' and points > 0:
            display_card()
            ask_player()
            earned_lost()
            overall_score()
        elif x == 'N' or points == 0:
            print('Thank you for playing')
"""


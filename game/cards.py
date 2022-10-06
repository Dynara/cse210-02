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
        

# 3) Display int between 1 to 13
    def display_card(self):
        self.value = random.randint(1, 13)
        return self.value

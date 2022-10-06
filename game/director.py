
from cards import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:

        
    """
    # Angela
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            
        """    
        
        # Create empty list to populate from class Card  
        self.playing_cards = []
        self.is_playing = True
        self.points = 0
        # Start Game with 300 for score
        self.total_score = 300

        # Making list of random card
        for i in range(2):
            card = Card()
            self.playing_cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
           

# Dylan
    def get_inputs(self):
        """Ask the user if the card is hi or lo

        """

        x = input('Do you wish to continue play: (y/n)').lower()
        
        """
        if x == 'y' and self.points > 0:
            display_card()
            ask_player()
            earned_lost()
            overall_score()
        elif x == 'n' or points == 0:
            print('Thank you for playing')
        """

# Francisco & Oghenekome       
    def do_updates(self):
        """Updates the player's overall score   
        The player earns 100 points if they guessed correctly.
        The player loses 75 points if they guessed incorrectly.
        If a player reaches 0 points the game is over        
        """
        if not self.is_playing:
            return  
        
        for i in range(len(self.playing_cards)):
            new_card = self.playing_cards[i]
            new_card.display_card()
        
        # Update total score
        self.total_score += self.points

        
# Stacie
    def do_outputs(self):
        """Displays next card and score
        """
        if not self.is_playing:
            return  

        # update value to what the next card is
        # value = card.display_card(self)
       
        values = []
        for i in range(len(self.playing_cards)):
            new_card = self.playing_cards[i]
            values += f"{new_card.value} "

        print(f"Next card was: {values[1]}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.total_score > 0)

        """
        # Display next card
        print(f"Next card was: {value}")
        # Display total score
        print(f"Your score is: {total_score}\n")
        """
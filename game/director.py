from functools import total_ordering
from optparse import Values
from game.cards import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:

        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            
        """
        card = Card()
        self.card = []
        self.is_playing = True
        self.score = 0
        # Start Game with 300 for score
        self.total_score = 300

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

        Args:
           self (Director): An instance of Director 
        """
        guess_card = input("higher or lower? [h/l] ").lower()
        if guess_card == "h" or guess_card == "l":
            print("Next card was")


        
# Stacie       
    def do_updates(self):
        """Updates the player's overall score

        Args:
            
        """
        if not self.is_playing:
            return  

        card.keep_playing()
      
        # Update score from the cards.earned_lost
        # score = cards.earned_lost()

        # Add the amount from earned_lost if positive
        # if self.cards.value > 0:        
        #   self.total_score += self.card.value
        # Subtract amount lost if negative
        # else:
        #   self.total_score -= self.card.value
         
        
# Stacie
    def do_outputs(self):
        """Displays . Also asks the player if they would like to keep playing

        Args:
            
        """
        if not self.is_playing:
            return  

        # update value to what the next card is
        values = card.display_card()
       
        # Display next card
        print(f"Next card was: {values}")
        # Display total score
        print(f"Your score is: {card.overall_score}\n")

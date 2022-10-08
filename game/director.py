
from game.cards import Card

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
        self.is_playing = True
        self.first_card = 0
        self.next_card = 0
        self.points = 300


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
        
        guess_card = input("higher or lower? [h/l] ").lower()
        if guess_card == "h" or guess_card == "l":
            print("Next card was")


        

# Francisco & Oghenekome       
    def do_updates(self):
        """Updates the player's overall score   
        The player earns 100 points if they guessed correctly.
        The player loses 75 points if they guessed incorrectly.
        If a player reaches 0 points the game is over        
        """
        if not self.is_playing:
            return  
        
        
        for i in range(len(self.first_card)):
            card = self.first_card
            card.roll()
        
        # Update points
        

        
# Stacie
    def do_outputs(self):
        """Displays next card and score
        """
        if not self.is_playing:
            return  

        # Display next card
        print(f"Next card : {self.next_card}")
        # Display points after round
        print(f"Your score is: {self.points}")
        # Ask player if they want to continue
        play_again = input("Play again? [y/n]")
        print()
        # Only continue if player says 'y' and have over 0 points
        self.is_playing = (play_again == 'y' and self.points > 0)
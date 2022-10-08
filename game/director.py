from game.cards import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean) : Whether or not the game is being played.
        points (int) : The score after one round of play.
        first_card ([Card]) : random integer (1,13)
        next_card ([Card]) : random integer (1,13)
        
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
        # class Card, display_card method
        self.first_card = Card.display_card(self)
        self.next_card = Card.display_card(self)

         # Initial card
        print(f"The card is: {self.first_card}")

        self.guess_card = input("higher or lower? [h/l] ").lower()


# Francisco & Oghenekome       
    def do_updates(self):
        """Updates the player's overall score   
        The player earns 100 points if they guessed correctly.
        The player loses 75 points if they guessed incorrectly.
        If a player reaches 0 points the game is over        
        """
        if not self.is_playing:
            return  
        
        
        # 2nd card is greater than first card, +100
        if self.guess_card == "h" and self.first_card <= self.next_card:
            self.points += 100
        # 2nd card is lower than first card, +100
        elif self.guess_card == "l" and self.first_card > self.next_card:
            self.points += 100
        # They guessed wrong
        else:
            self.points -= 75
        
        # Couldn't get this to work because there is no list/length        
        #for i in range(len(self.first_card)):
        #    card = self.first_card
        #    card.roll()

        
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
        
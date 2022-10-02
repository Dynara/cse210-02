#Cards code
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

#Director code
def get_input(self):
    print('Higher or lower?')
    guess_card = input()
    if guess_card == 'higher' or guess_card == 'lower':
        print('The card is')

# Rock Paper Scissors project
import random
def play():
    user = input("What's your choice ? 'r' for Rock, 's' for Scissors, 'p' for Paper.\n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "Tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"
    
def is_win(player,opponent):
    #return true if players win
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print (play())
"""
This program is a Rock Paper Scissor Game"
"""
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  else:
    print message["lost"]
    
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
  
play_RPS()
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Rock, paper, scissors?")

while True:
	play = "Enter 'q'  to quit."
	if player == 'q':
		break

			
print(play)
print("player: ", player)
print("computer: ", computer)



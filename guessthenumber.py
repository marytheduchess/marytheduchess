#freecodecamp project called guess the number
# ~ import random
#random.randin(a, b) is what we use and LOOPS
import random
def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input('Guess a number between 1 and {x}: '))
		if guess < random_number:
			print('Sorry, guess again. Too low.')
		elif guess > random_number:
			print('Sorry, guess again. Too high.')
print('Yay, congrats. You have guessed the number {random_number} correctly.')
		
		

guess(10)

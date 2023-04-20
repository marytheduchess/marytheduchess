#pg. 120 
# ~ height = input("How tall are you in inches? ")
# ~ height = int(height)

# ~ if height >= 36:
	# ~ print("\nYou're tall enough to ride!")
# ~ else:
	# ~ print("\nYou'll be able to ride when you're a little taller.")
	
#modulo operator pg. 120, a useful tool for working w numerical info is the modulo operator (%), which divides one number by another and returns the remainder
#it doesn't tell you how many times one numbre fits into another, it just tells you the reainder

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")


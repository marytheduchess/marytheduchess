## str.format = optional method that gives users more control when displaying output
animal = "cow"
item = "moon"

# ~ print("The "+ animal +  "jumped over the " + item ".")
# ~ print("The {} jumped over the {}.".format(animal, item))

# ~ #positional argument
# ~ print("The {1} jumped over the {1}.".format(item, animal))

#keyword arg
# ~ print("The {animal} jumped over the {item}".format(animal='cow', item='moon'))
# ~ print("The {animal} jumped over the {animal}".format(animal='cow', item='moon'))

# ~ text = "The {} jumped over the {}."
# ~ print(text.format(animal, item))

# ~ name = "Bro"
# ~ print("Hello my name is {}".format(name))
# ~ print("Hello my name is {:>10}. Nice to meet you".format(name)) #to align to the left
# ~ print("Hello my name is {:<10}. Nice to meet you".format(name)) #to align to the right


# ~ #formatting numbers
# ~ number = 3.14159
# ~ print("The number pi is {:.3f}".format(number)) #f is floating point number (decimal), also rounds

# ~ numbers = 1,000

# ~ print("The number is {}".format(numbers))
# ~ print("The number is {:o}".format(numbers))
# ~ print("The number is {:E}".format(numbers)) #scientific notation

####

import random

x = random.randint(1, 6)
print(x)
y = random.random() #generates a random number
print(y)


myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) #
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards) #shuffle method (shuffled cards)
print(cards)

##useful methods for the random module



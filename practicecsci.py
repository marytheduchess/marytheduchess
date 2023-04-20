# ~ count = 15
# ~ sentence = "Okay so what's up dude? I haven't seen you in a while!''"
# ~ print(sentence)
# ~ for char in sentence:
	# ~ if char == 'b' or char == 'e':
		# ~ count +=1

class Solution():
	def __init__(self, count, sentence):
		self.count = 0
		self.sentence = sentence
		
	def gimmeone(self):
		self.sentence = "hello, how are you today? what's going on?"
		print(self.sentence)
			
	def gimmetwo(self):
		for char in self.sentence:
			if char == 'h' or char == 'o':
				self.count += 1
		print(self.count)
		
solve = Solution(0, ' ')
solve.gimmeone()
solve.gimmetwo()


def count_down():
	counting = int(input("Hello, pick a number:"))
	print(counting)
	for counting in range(10, -10):
		print("Wow, you're in range!'")
		
count_down()


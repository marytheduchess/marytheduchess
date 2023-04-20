
value = input("\nPick a number and I'll return it as a roman numeral!")

class Solution:
	def __init__(self, s, value):
		self.symbol = symbol
		self.answer = answer
		
	def roman_to_int(self):
		symbol = {
			'I': '1',
			'IV': '4',
			'V': '5',
			'IX': '9',
			'X': '10',
			'XL': '40',
			'L': '50',
			'XC': '90',
			'C': '100',
			'CD': '400',
			'D': '500',
			'CM': '900',
			'M': '1000',
			}
		i = 0
		value = 0
		while i < len(s):
			if i+1<len(s) and s[i:i+2] in symbol:
				value+=symbol[s[i:i+2]]
				i+=2
			else:
				print(s)
				value+=symbol[s[i]]
				i+=1
			return value
 
ob1 = Solution(s, value)
print(ob1.roman_to_int())











	

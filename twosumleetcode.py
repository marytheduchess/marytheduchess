####
##"Two Sum" LeetCode problem
##//leetcode.com/problems/two-sum/

# ~ class TwoSum:
	# ~ def __init__(self, list1, target):
		# ~ self.list1 = list1
		# ~ self.target = target
		
	# ~ def solution(self):
		# ~ length = len(list1)
		
		# ~ for i in range(length-1):
			# ~ for j in range (i+1, length):
				# ~ if list1[i] + list1[j] == self.target:
					# ~ new_list = i, j
					# ~ return list(new_list)
					
		# ~ return -1
		
# ~ list1 = [1, 2, 4, 5, 11]
# ~ target = 6
# ~ obj = TwoSum(list1, target)
# ~ print(obj.solution())
###this is how you do the problem

##
class TwoSum:
	def __init__(self, list2, target):
		self.list2 = list2
		self.target = target
		
	def solution(self):
		length = len(list2)
		
		for i in range(length+1):
			for j in range(i-1, length):
				if list2[i] - list2[j] == self.target:
					new_list = i, j
					return new_list
					
		return +1
		
list2 = [15, 11, 7, 2]
target = 9
obj = TwoSum(list2, target)
print(obj.solution())
	
		

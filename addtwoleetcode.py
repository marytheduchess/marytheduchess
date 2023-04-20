# ~ mylist = [1, 2, 3, 4, 5, 6]
# ~ b = [i*i for i in mylist]

# ~ print(mylist)
# ~ print(b)



# ~ mylist2 = [5, True, "apple", "apple"]
# ~ print(mylist2)
# ~ item = mylist[-1]
# ~ print(item)



#Tuples = ordered, immutable lists. cannot be changed, used for objects that belong together
# ~ mytuple = tuple(["Max", 28, "Boston"])
# ~ print(mytuple)

# ~ if "max" in mytuple:
	# ~ print("yes")
# ~ else:
	# ~ print("no")

# ~ my_tuple = ['a', 'x', 'y', 'w', 'p']
# ~ print(my_tuple.index('p'))


#itertools: product, permutations, combos, accumulate, groupy
# ~ from itertools import permutations
# ~ a = [1, 2, 3]
# ~ perm = permutations(a, 2)
# ~ print(list(perm))
# ~ from itertools import combinations, combinations_with_replacement
# ~ a = [1, 2, 3, 4]
# ~ comb = combinations(a, 2)
# ~ print(list(comb))
# ~ comb_wr = combinations_with_replacement(a, 2)
# ~ print(list(comb_wr))

# ~ from itertools import accumulate
# ~ import operator
# ~ a = [1, 2, 5, 3, 4]
# ~ acc = accumulate(a, func=operator.mul)
# ~ acc = accumulate(a, func=max)
# ~ print(a)
# ~ print(list(acc))

# ~ from itertools import groupby
# ~ persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
			# ~ {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
		

# ~ group_obj = groupby(persons, key=lambda x: x['age'])
# ~ for key, value in group_obj:
	# ~ print(key, list(value))

# ~ from itertools import count, cycle, repeat
# ~ a = [1, 2, 3]

# ~ for i in repeat(1, 4):
	# ~ print(i)
	

	
		
	


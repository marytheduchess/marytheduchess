def sales_bonuses():
	sales_type = input("Enter sales type: ")
	sales_bonus = input("Enter sales bonus: ")
	
	if sales_type == 2:
		if sales_bonus < 5:
			sales_bonus = 10
		else:
			sales_bonus = sales_bonus + 2
	else:
		sales_bonus = int(sales_bonus) + 1
sales_bonuses()



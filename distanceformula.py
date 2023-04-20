# ~ #pg. 48

# ~ x1 = float(input('Enter x1: '))
# ~ y1 = float(input('Enter y1: '))
# ~ x2 = float(input('Enter x2: '))
# ~ y2 = float(input('Enter y2: '))
# ~ h_dist = x2 - x1
# ~ v_dist = y2 - y1
# ~ dist = (h_dist ** 2 + v_dist ** 2) ** 0.5
# ~ print("The distance is ", dist)

## "Decisions and Looping"
##pg. 53
# ~ n = int(input("Enter your age: "))
# ~ if n > 30:
	# ~ print("Don't trust anyone over 30.")
##pg.54 
# ~ def is_even(n):
	# ~ remainder = n % 2
	# ~ if remainder == 0:
		# ~ print('n is even')

# ~ is_even(2)
# ~ is_even(15)
# ~ is_even(202)
# the function is_even() either prints the messasge n is even or it deos nothing. 
# lets review the key parts
## /-^-/ first this code uses 'remainder' division  -- % --(aka 'mod' division and the %, a 'modulo')
#  it's used to divide by 2, in this case and produces the remainder
## /-^-/ the 'if' statement uses double equal signs -- == -- to compare the value to zero
##/-^- this is an important rule in Python, as in the C family of languages.
## /-^-/ the single equal sign -- = -- specifies assignment
## /-^-/ double equal signs -- == -- specify tests for equality and return either 'true' or 'false'
	# //-^-//	if remainder ==:
	# //-^-//		print('n is even')
## /-^-/ what qualifies as a 'condition'? 
## /-^-/ in general, a 'condition' is a comparison between two values (which also incl. '>' or '<', etc.)
## /-^-/ or, it's a combination of comparisons joined by the "'Boolean' operators" 'and', 'or', and 'not'.
## Here's another example:
# //-^-//
# //-^-// if age > 12 and age < 20:
	# //-^-// print('Wow!')
	# //-^-// print('You are a teenager.')
## /-^-/ the 'condition' after the 'if' keyword is presumed to have a value that is 'true' or 'false',
## /-^-/ so normally, you'd use a 'condition' such as n > 3. 
# /-^-/ however, you can use any valid expression, and Python will convert to a 'Boolean' ('True' or 'False')
# /-^-/ as well as it can. For 'numeric values', 'zero' is converted to 'false'; 
# /-^-/ other values are converted to 'true'. Also, the special value 'none' is converted to 'false'
# /-^-/ while most non-numeric values are converted to 'true'.
do_more = True
if n > 3:
	do_more = False

if do_more:
	print('n is not greater than 3.')

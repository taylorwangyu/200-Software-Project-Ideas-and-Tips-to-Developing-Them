# Numbers problem 4
# Title: Change Return Program
# Difficulty: 2
# Description: Create a program where it shows the user a list of items to buy and their price. 
# Then ask the user to pick an item and enter in the amount of money they would have inserted into 
# the "vending machine". Have the program calculate the change and return it to the user in the 
# form of quarters, dimes, nickels and pennies. For example, if the user chooses an item that 
# costs $1.25 and they say they give it $2.07 the program would print out 3 quarters, 1 nickel 
# and 2 pennies as change for the user.

cost = raw_input("How much does the item cost?")
give = raw_input("How much does the customer give?")

cost = float(cost) * 1000
give = float(give) * 1000

diff = int(give - cost) / 10
if (diff < 0):
	print "WTF!"
else: 
	if (diff == 0):
		print "Just cover it"
	else:
		result = ''
		# quarters
		temp_q = diff / 25
		diff = diff % 25
		if (temp_q != 0):
			result += str(temp_q)+' quarters '
		if (diff != 0):
			temp_d = diff / 10
			diff = diff % 10
			if (temp_d != 0):
				result += str(temp_d)+' dimes '
			if (diff != 0):
				temp_n = diff / 5
				diff = diff % 5
				if (temp_n != 0):
					result += str(temp_n)+' nickels '
				if (diff != 0):
					result += str(diff)+' pennies '
		print result

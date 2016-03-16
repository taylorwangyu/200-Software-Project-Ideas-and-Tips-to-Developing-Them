# Title: Credit Card Validator
# Difficulty: 6
# Description: How do we know that the credit card number someone entered on our store is correct? 
# How do we know it is valid for the type of credit card they specified? Create a program which 
# allows the user to specify a credit card number and the card type (Visa, Mastercard, American Express or Discover) 
# and return a message if the number is valid or an error message if the credit card number is invalid.

card_number = raw_input("Input your card number:\n")
sum = 0
l = len(card_number)
if (l >= 16)and(l <= 19)and(cmp(card_number[0:2],"62") == 0):
	print "China UnionPay"
if (l == 16)and(int(card_number[0:2]) >= 51)and(int(card_number[0:2]) <= 55):
	print "Mastercard"
if (((l == 13) or (l == 16) or (l == 19)) and (card_number[0] == '4')):
	print "Visa"
even = False
for i in range(l-1,-1,-1):
	t = int(card_number[i])
	if (even):
		if (t * 2 >= 10):
			sum += t * 2 - 9
		else:
			sum += t * 2
		even = False
	else:
		sum += t
		even = True
if (sum % 10 == 0):
	print "Credit card number is valid"
else:
	print "Credit card number is invalid"
# Numbers Problem 3
# Title: Binary to Decimal and Back Converter
# Difficulty: 4
# Description: Make a program which has the user enter in either a decimal value and prints out its binary equivalent or enter a binary value and it prints out the decimal equivalent value.

input_type = raw_input("what's type of your input(Binary/Decimal):")
if (input_type == "Binary"):			#Binary to Decimal
	num = raw_input("Input number:")
	convert_num = 0
	for ch in num:
		convert_num = convert_num * 2 + int(ch)
	print convert_num
else:									#Decimal to Binary
	num = raw_input("Input number:")
	temp = 0
	for ch in num:
		temp = temp * 10 + int(ch)
	result = ''
	while (temp>0):
		result = str(temp % 2) + result
		temp = temp / 2
	print result
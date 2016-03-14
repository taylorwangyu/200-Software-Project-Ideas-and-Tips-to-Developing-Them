# Numbers problem 1
# Description: 
# This project involves working with fractions. How do you add 1/3 + 1/5? Create a program that 
# first asks the user which operation they want to do: add, subtract, multiply or divide and 
# then asks for 1, 2 or more fractions to work with. The program prints out the result.

def gcd(a,b):
	if (a%b == 0):
		return b
	else:
		return gcd(b,a%b)


string = raw_input("Input the expression:\n")

numerator_1 = 0
numerator_2 = 0
denominator_1 = 0
denominator_2 = 0

flag = 0
calc_type = 0
for char in string:
	if (char == '/')and(flag == 1):
		calc_type = 4
		flag = flag + 1
		continue
		
	if (char == '/'):
		flag = flag + 1
		continue
	
	if (char == '+'):
		calc_type = 1
		flag = flag + 1
		continue
	if (char == '-'):
		calc_type = 2
		flag = flag + 1
		continue
	if (char == '*'):
		calc_type = 3
		flag = flag + 1
		continue
	

	if ((char != '/')and(flag == 0)):
		numerator_1 = numerator_1 * 10 + int(char) - int('0')
	if ((char != '/')and(flag == 1)):
		denominator_1 = denominator_1 * 10 + int(char) - int('0')
	if ((char != '/')and(flag == 2)):
		numerator_2 = numerator_2 * 10 + int(char) - int('0')
	if ((char != '/')and(flag == 3)):
		denominator_2 = denominator_2 * 10 + int(char) - int('0')
	
if (calc_type == 1):
	gcd_number = gcd(denominator_1,denominator_2)
	denominator_3 = denominator_1 * denominator_2 / gcd_number
	numerator_3 = numerator_1 * (denominator_3 / denominator_1) + numerator_2 * (denominator_3/denominator_2)
	scale = gcd(denominator_3,numerator_3)
	print str(numerator_3/scale)+"/"+str(denominator_3/scale)
if (calc_type == 2):
	gcd_number = gcd(denominator_1,denominator_2)
	denominator_3 = denominator_1 * denominator_2 / gcd_number
	numerator_3 = numerator_1 * (denominator_3 / denominator_1) - numerator_2 * (denominator_3/denominator_2)
	if (numerator_3 == 0):
		print 0
	else:
		scale = abs(gcd(denominator_3,numerator_3))
		print str(numerator_3/scale)+"/"+str(denominator_3/scale)
if (calc_type == 3):
	numerator_3 = numerator_1 * numerator_2
	denominator_3 = denominator_1 * denominator_2
	scale = gcd(denominator_3,numerator_3)
	print str(numerator_3/scale)+"/"+str(denominator_3/scale)
if (calc_type == 4):
	numerator_3 = numerator_1 * denominator_2
	denominator_3 = denominator_1 * numerator_2
	scale = gcd(denominator_3,numerator_3)
	print str(numerator_3/scale)+"/"+str(denominator_3/scale)
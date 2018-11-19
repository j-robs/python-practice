prompt = "Enter a number: "
num = raw_input(prompt)

if int(num) % 4 == 0:
	print "Your number is even, and a multiple of 4!"
elif int(num) % 2 == 0:
	print "Your number is even."
else: 
	print "Your number is odd."
	
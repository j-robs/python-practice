a = [1, 2, 4, 6, 1, 66, 78, 16, 2, 5]
b = []

prompt = "Enter a number: "
num = raw_input(prompt)

#for item in a:
	#if item < int(num):
		#b.append(item)
	#else:
		#continue
#print b

b.append([aa for aa in a if aa < int(num)])
print b
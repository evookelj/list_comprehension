upper = [[chr(i) for i in range(65,90)], False]
lower = [[chr(i) for i in range(97,122)], False]
digits = [[str(i) for i in range(0,10)], False]

def threshold(password):
	for i in password:
		if i in upper[0]:
			upper[1] = True
		if i in lower[0]:
			lower[1] = True
		if i in digits[0]:
			digits[1] = True
	return upper[1] and lower[1] and digits[1]

def strength(password):
	ret=1
	up=0
	low=0
	for i in password:
		if i in upper[0]:
			upper+=1
		ret+=(1/(len(password))
		for i in low:
			low+

print threshold("Hello WorLd")

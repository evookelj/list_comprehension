upper = [[chr(i) for i in range(65,91)], False]
lower = [[chr(i) for i in range(97,123)], False]
digits = [[str(i) for i in range(0,10)], False]
other = [chr(i) for i in range (33,65) if i not in digits]

for i in other:
	print i

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
	dig=0
	others=0
	for i in password:
		if i in upper[0]:
			up+=1
		if i in lower[0]:
			low+=1
		if i in digits[0]:
			dig+=1
		if i in other:
			others+=1
	if up>0 and low>0:
			ret+=3
	if dig>0:
			ret+=3
	if others>0:
			ret+=3
	return ret


print strength("hI!0")

def add(a, b):
	print("ADDITION {}+{}".format(a,b))
	return a + b

def subtract(a, b):
	print("SUBTRACTION {}-{}".format(a,b))
	return a -b

def multiply(a, b):
	print("MULTIPLICATION {}*{}".format(a,b))
	return a * b

def divide(a, b):
	print("DIVISION {}/{}".format(a,b))
	return a / b

print("Basic Operations using functions!")

age = add(86,46)
height = subtract(78,64)
weight = multiply(36,48)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

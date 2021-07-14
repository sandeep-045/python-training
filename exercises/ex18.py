# arguments are stored in pointer
def function1(*args):
	arg1,arg2 = args
	print("Value 1: "+arg1+"\nValue2: "+arg2)

#arguments are pointerless,stored in variable
def function2(arg1,arg2):
	print("Value 1: "+arg1+"\nValue2: "+arg2)

#only one argument
def function3(arg1):
	print("Value 1: "+arg1)

#No arguments
def function4():
	print("Nothing !!")

#function calling

function1("Sandeep","Consultadd")
function2("Sandeep","Consultadd")
function3("Sandeep")
function4()
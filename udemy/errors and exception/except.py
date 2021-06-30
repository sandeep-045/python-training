x=int(input())

try:
    x+2
except TypeError as e:
    print(e)
else:
    print("addition successful")
finally:
    print("I am in because I'm in")
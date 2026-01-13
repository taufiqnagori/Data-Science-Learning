#Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("a is not greater than b")


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 5
z = ""          #Empty string returns false
print(bool(x))
print(bool(y))
print(bool(z))


#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:
def myfunction() :
  return True

print(myfunction())


#isinstance()
x = 200
print(isinstance(x, int))
# Creating Variable
x = 5           # here 'x' is Variable (Integer)
y = "taufiq"    # here 'y' is Variable (String)
print(x)
print(y)


# Casting
x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0


# Get the type {(type()}
m = 5
n = "taufiq"
print(type(m))
print(type(n))

#Case Sensitive
a = 5
A = "John"
print(a)
print(A)        # A will not overwrite a


# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Multi Words Variable Names
#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"


# Many values to Multiple Varaibles
d,e, f = "Orange", "Banana", "Mango"
print(d)
print(e)
print(f)

# One Value
g = h = i = "orange"
print(g)
print(h)
print(i)

#Unpack a Collection
fruits = ["apple", "banana", "mango"]
j, k, l = fruits
print(j)
print(k)
print(l)

o = 5
p = 6
print(o + p)        # It will perform addition


#Global Variable
q = "awesome"

def myfunc():
    print("Python is " + q)

myfunc()

#Exa
r = "awesome"

def myfun():
    r = "fantastic"
    print("Python is " + r)

myfun()
print("Python is " + r)


# Global Keyword
t = "awesome"

def myfunct():
  global t
  t = "fantastic"

myfunct()

print("Python is " + t)
'''Numbers

There are three types of no:
int -- x = 1
float -- y = 1.23
complex -- z 1j
'''

#type conversion
x = 1           #int
y = 2.8         #float
z = 1j          #complex

#convert from int to float
a = float(x)

#convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Random Number
import random
print(random.randrange(1, 10))


#specify a Variable type
x1 = int(1)   # x will be 1
y1 = int(2.8) # y will be 2
z1 = int("3") # z will be 3
x2 = float(1)     # x will be 1.0
y2 = float(2.8)   # y will be 2.8
z2 = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x3 = str("s1") # x will be 's1'
y3 = str(2)    # y will be '2'
z3 = str(3.0)  # z will be '3.0'

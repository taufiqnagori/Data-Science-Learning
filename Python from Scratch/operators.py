"""Python Operators
Operators are used to perform operations on variables and values."""

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)

print("\n")

"""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators"""

"""Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator    	Name	        Example	
+	            Addition	    x + y	
-	            Subtraction	    x - y	
*	            Multiplication	x * y	
/	            Division	    x / y	
%	            Modulus	        x % y	
**	            Exponentiation	x ** y	
//	            Floor division	x // y"""

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

print("\n")


"""Division in Python
Python has two division operators:

/ - Division (returns a float)
// - Floor division (returns an integer)"""
x = 12
y = 5

print(x / y)

a = 12
b = 5

print(a // b)
print("\n")



"""Assignment Operators
Assignment operators are used to assign values to variables:

Operator	    Example	        Same As	
=	            x = 5	        x = 5	
+=	            x += 3	        x = x + 3	
-=	            x -= 3	        x = x - 3	
*=	            x *= 3	        x = x * 3	
/=	            x /= 3	        x = x / 3	
%=	            x %= 3	        x = x % 3	
//=	            x //= 3	        x = x // 3	
**=	            x **= 3	        x = x ** 3	
&=	            x &= 3	        x = x & 3	
|=	            x |= 3	        x = x | 3	
^=	            x ^= 3	        x = x ^ 3	
>>=         	x >>= 3	        x = x >> 3	
<<=	            x <<= 3	        x = x << 3	
:=	            print(x := 3)	x = 3 print(x)
"""

# Initial value
x = 10
print("Initial x =", x)

# = (Assignment)
x = 5
print("=  :", x)

# += (Add and assign)
x = 10
x += 3
print("+= :", x)

# -= (Subtract and assign)
x = 10
x -= 3
print("-= :", x)

# *= (Multiply and assign)
x = 10
x *= 3
print("*= :", x)

# /= (Divide and assign)
x = 10
x /= 3
print("/= :", x)

# %= (Modulus and assign)
x = 10
x %= 3
print("%= :", x)

# //= (Floor division and assign)
x = 10
x //= 3
print("//=:", x)

# **= (Exponent and assign)
x = 10
x **= 3
print("**=:", x)

# &= (Bitwise AND and assign)
x = 10
x &= 3
print("&= :", x)

# |= (Bitwise OR and assign)
x = 10
x |= 3
print("|= :", x)

# ^= (Bitwise XOR and assign)
x = 10
x ^= 3
print("^= :", x)

# >>= (Right shift and assign)
x = 10
x >>= 2
print(">>=:", x)

# <<= (Left shift and assign)
x = 10
x <<= 2
print("<<=:", x)

# := (Walrus operator)
print(":= :", (y := 20))
print("y =", y)

#The Walrus Operator
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print("\n")



"""
Comparison Operators
Comparison operators are used to compare two values:

Operator	    Name	                    Example	
==	            Equal	                    x == y	
!=	            Not equal	                x != y	
>	            Greater than	            x > y	
<	            Less than	                x < y	
>=	            Greater than or equal to	x >= y	
<=	            Less than or equal to	    x <= y
"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Chaining Comparison Operators
x = 5

print(1 < x < 10)

print(1 < x and x < 10)
print("\n")


'''Logical Operators
Logical operators are used to combine conditional statements:

Operator    	Description              	                                    Example	
and 	        Returns True if both statements are true	                    x < 5 and  x < 10	
or	            Returns True if one of the statements is true	                x < 5 or x < 4	
not	            Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)'''

x = 10
y = 5

# Logical AND
print(x > 5 and y > 3)     # True and True → True

# Logical OR
print(x < 5 or y > 3)      # False or True → True

# Logical NOT
print(not (x > 5))         # not True → False

# Logical AND with False
print(x < 5 and y > 3)     # False and True → False

# Logical OR with False
print(x < 5 or y < 3)      # False or False → False

# NOT operator example
print(not (x == y))        # not False → True

print("\n")


"""Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	       Description	                                            Example	
is 	               Returns True if both variables are the same object	    x is y	
is not	           Returns True if both variables are not the same object	x is not y"""

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Identity operator: is
print(x is y)        # False (different memory locations)
print(x is z)        # True  (same memory location)

# Identity operator: is not
print(x is not y)    # True
print(x is not z)    # False

print("\n")

"""Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal"""


"""Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	                                                                        Example	
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y"""

x = [1, 2, 3, 4, 5]

# Membership operator: in
print(3 in x)        # True
print(10 in x)       # False

# Membership operator: not in
print(3 not in x)    # False
print(10 not in x)   # True

#Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


"""Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description	                                                                                                Example	
& 	        AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is 1	                                                                x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1                                                            	x ^ y	
~	        NOT	                    Inverts all the bits	                                                                                    ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
>>      	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2"""


x = 10   # 1010 in binary
y = 3    # 0011 in binary

# Bitwise AND
print(x & y)      # 0010 → 2

# Bitwise OR
print(x | y)      # 1011 → 11

# Bitwise XOR
print(x ^ y)      # 1001 → 9

# Bitwise NOT
print(~x)         # -(x+1) → -11

# Left Shift
print(x << 1)     # 10100 → 20

# Right Shift
print(x >> 1)     # 0101 → 5




"""Operator Precedence
Operator precedence describes the order in which operations are performed.

Precedence Order
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	                        Description	Try it
()	                                Parentheses	
**	                                Exponentiation	
+x  -x  ~x	                        Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                        Multiplication, division, floor division, and modulus	
+  -	                            Addition and subtraction	
<<  >>	                            Bitwise left and right shifts	
&	                                Bitwise AND	
^	                                Bitwise XOR	
|	                                Bitwise OR	
==  !=  >  >=  <  <=             	Comparisons, identity, and membership operators	
is  is not  in  not in
not	                                Logical NOT	
and	                                AND	
or	                                OR	



Left-to-Right Evaluation
If two operators have the same precedence, the expression is evaluated from left to right.
"""
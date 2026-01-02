#5
# #Strings
print("Hello World")
print('Hello World')

print("It's alright")
print("He is Called 'John'")
print('He is called "John"')

#Assign String to a Variable
a = "Hello"
print(a)


#Multi Line String
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)


#String are Array.
c = "Hello World"
print(a[1])


# Looping through a string
for x in "banana":
    print(x)


#String Length
#Note: The first character has index 0
d = "Hello World!"
print(len(d))


#Check String
txt = "The Best thing in life are free!"
print("free" in txt)

#using if statement
txt = "The Best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#using if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Python Slicing
e = 'Hello, World!'
print(e[2:5])

#Slice from the start
f = 'Hello, World!'
print(f[:5])

#Slice to the end
g = 'Hello World'
print(g[2:])


#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
h = 'Hello World'
print(h[-5:-2])


#Modify Strings
#Upper Case
i = "Hello, World!"
print(i.upper())

#lower case
i = "Hello, World!"
print(i.lower())

#Remove Whitespace
j = 'Hello World!'
print(j.strip())

#Replace String
k = "Hello World"
print(k.replace("H", "J"))

#Split String
l = "Hello, World"
print(l.split(","))


#String Concatenation
m = "Hello"
n = "World"
o = m +" "+ n
print(o)


# Format - String
#string format

#age = 36
#ttx = "My name is Taufiq, I am " + age
#print(ttx)    //This will produce an error:

#F-Strings
age = 22
ttx = f"My name is Taufiq, I am {age}"
print(ttx)


#Placeholders and Modifier
price = 100
txt = f"The price is {price} rupes"
print(txt)

price = 100
txt = f"The price is {price:.2f} dollars"
print(txt)

#It can do Operation
txt = f"The price is {20 * 59} dollars"
print(txt)


#Escape Character
#txt = "We are the so-called "Vikings" from the north." //This will generate error

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Characters
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value	
"""



#String Methods
"""
Python has a set of built-in methods that you can use on strings.
Note: All string methods return new values. They do not change the original string.

Method             	Description
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()         	Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()      	Returns true if the string ends with the specified value
expandtabs()      	Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()            	Fills the string with a specified number of 0 values at the beginning
"""
#1
var1=10
#Check the memory address of var1
print(hex(id(var1)))

#2
var1=100
#Check the memory address of var1 again
print(hex(id(var1)))

#Explanation:
#When first assigning var1=10, Python creates an integer with the value 10 and connects var1 to its referral.
#When assigning var1=100, I reassign the variable var1 to a different integer (100), meaning that the original integer (10) is not relevant to the variable anymore.

#3
var2=100
print(hex(id(var2)))
#Check the id() of the value 100 to see if it still matches var2.
print(f"Address of var2: {hex(id(var2))}")
print(f"Address of literal 100: {hex(id(100))}")
#Used the existing one

#4:Memory addresses for str1 and str2
str1="Hello"
str2="World"

#Addresses in hexadecimal Char
print(f"Address of str1[0]:{hex(id(str1[0]))}")
print(f"Address of str1[1]:{hex(id(str1[1]))}")
print(f"Address of str2[0]:{hex(id(str2[0]))}")
print(f"Address of str2[1]:{hex(id(str2[1]))}")

#5 Problem-Solving
#Variable Operations: Without solving in Python,
# x + y = xy
# "the" + x + "chases the" + y = thexchasesthey
# x * 4 = xxxx

# Increment Statement:
# If x = 50, increment x by 1
# x = x + 1
# 51 - 50 + 1

#6 Troubleshooting
# Without Python:
# hello= "hello" : True. This is a working string assignment
# _var=100 : True. Variables can begin with an underscore
# !var_1=200 : False. Variables cannot start with a "!"
# print= "print me" Works sometimes. Using a built-in function as a variable. It cannot be used in later code.
# false= 0 : False. "False" cannot be used as a variable in Python because it is a reserved keyword.


#Challenges
#After each time I'd input the code and let it run, I would get random numbers and letters instead of 10/100
#I did not understand the addition of the (hex(id)) aspect of the code. After a quick Google search, the 'id()' function makes a memory become an integer and 'hex()' turns the integer into a hexadecimal representation.
#Even after watching the lecture, I had a hard time understanding hexadecimal representations, so I had to do further research to understand it better.
#I had some confusion with the troubleshooting part of this assignment. Specifically the print= "print me," because I could not find a clear answer online.
#For some of the questions, I did not know whether to make them as notes or write the code itself. Initially, I had errors in my code, so I decided to make it all #.
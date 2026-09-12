#1. Comparison Operators
print(2<5)
print(10<=10)
x=10
print(20<x)
print("A"<"a")
print("Monday">"Tuesday")

#2. Logical Operators (and,or,not)
print(10>4 and 50<100)
print(10<4 and 50<100)
print(10<4 or 50>10)
print(10>4 and 50>100)
print(10<4 or 50>100)
print(10>4 and 50>100)
print(10>4)
print(not(10>4))

#3.Bitwise logical operators (and,or,not,xor)
x=0b1110
y=0b1011
result = x|y
print(result)
print(bin(result))

#4. Decision Statements
number1=int(input("Enter a number: "))
number2=int(input("Enter a second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("The larger number is:",larger_number)

x=10
if x>5:
    if x==6:
        print("nested: x==6")
    elif x==10:
        print("nested: x==10")
    else:
        print("nested: else")
else:
    print("else")

#5. Problem-Solving
#5a. Find the largest three integers using just "if" statements
number1=int(input("Enter an integer: "))
number2: int = int(input("Enter another integer: "))
number3: int = int(input("Enter another integer: "))
largest= number1
if number2>largest:
    largest = number2
if number3> largest:
    largest = number3

print("The largest number is:",largest)

#5b. Even or odd
number= int(input("Enter a number: "))
#1
if number % 2 == 0:
    print("Attempt 1: Even")
else:
    print("Attempt 1: Odd")

#2
if (number // 2) * 2 == number:
    print("Attempt 2: Even")
else:
    print("Attempt 2: Odd")

#3
if (number & 1)==0:
    print("Attempt 3: Even")
else:
    print("Attempt 3: Odd")

#5c. CISC 179 Grading Scheme:
percent= int(input("Enter a percentage: "))

if percent>90:
    print("Grade: A - Work of genuinely superior quality")
elif percent>=80:
    print("Grade: B - Passing performance falls approximately in the upper distribution of all passing grades")
elif percent>=71:
    print("Grade: C - Passing performance falls approximately in the center of the distribution of all passing grades")
elif percent>=65:
    print("Grade: D = Passing performance falls approximately in the lower distribution of passing grades")
else:
    print("Grade: F - Failing performance that does not satisfy the basic requirements of the course and needs to be improved in significant ways.")

#5d. Truth Tables
op= input("Enter a logical operator (and,or,not):")
if op=="and":
    print("A | B | A and B")
    print(f"True | True |{True and True}")
    print(f"True | False | {True and False}")
    print(f"False | True | {False and True}")
    print(f"False | False | {False and False}")
elif op=="or":
    print("A | B | A and B")
    print(f"True | True |{True or True}")
    print(f"True | False | {True or False}")
    print(f"False | True | {False or True}")
    print(f"False | False | {False or False}")
elif op=="not":
    print("A | B | A and B")
    print(f"True | True |{True or True}")
    print(f"True | False | {True or False}")
    print(f"False | True | {False or True}")
    print(f"False | False | {False or False}")
else:
    print("Unable to print logical operator")

#5e. Even or Odd with Bitwise AND
number=int(input("Enter a number: "))
if (number&1) == 0:
    print("Number is even")
else:
    print("Number is odd")

#6: Code Revision
name=input("What's your name?")
time=int(input("What time is it?"))

if (time<1200):
    print("Hi" + name + ", good morning!")
elif(time<1800):
    print("Hi" + name + ", good afternoon!")
else:
    print("Hi" + name + ", good evening!")
    print("Good Bye")

#7: Output verification
#Without using Python, the output of the code will be:
# one
# two


#Challenges
#I had lots of trouble with the revision section of this assignment. I used trial and error to get to a program that worked
#For some of the code, I accidentally put the colon on the inside of the parenthesis, giving me a faulty line of code (seen in lines 130,132,& 134)
# I had a typo on line 33 that did not permit my code from proceeding. I wrote larger_number2= number2 instead of larger_number=number2
#I used quotations in all of my print statements and for some of the inequalities I would get false though it was true. To fix this I made a quick Google Search and learned that putting values in quotations treats them in numerical order, overriding what I first put
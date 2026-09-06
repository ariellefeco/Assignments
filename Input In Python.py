#1. User Input

#A. Kilograms to pounds
kilograms = float(input("Enter weight in kilograms: "))
#Calculate pounds
pounds = kilograms * 2.2
#Output: Weight in pounds
print(f"The equivalent weight in pounds is: {pounds}")

#B. Credit card interest
netBalance = float(input("Balance shown in the bill: "))
payment = float (input("Payment made: "))
d1= int(input("The number of days in the billing cycle (d1): "))
d2= int(input("The number of days payment is made before the billing cycle (d2):"))
interestRate = float (input("Enter monthly interest rate (e.g., 0.0152): "))

#Calculate average daily balance:
averageDailyBalance = (netBalance * d1 - payment * d2) / d1
#Calculate interest:
interest = averageDailyBalance * interestRate
#Output
print(f"Interest on the unpaid balance is: {interest}")

#2: Troubleshooting
#Without using Python:
#a. hello = "Hello" : Correct. This is true because it is a working string statement.
#b. _var = 100 : Correct. This works because variables can begin with an underscore.
#c. !var_1 = 200 : Incorrect. Variables cannot begin with a character like "!"
#d. print = "print me" : Sometimes correct. Using this program will prevent you from using the function 'print()' later.
#e. False = 0 : Incorrect. False cannot be used as a variable name because it is a reserved keyword in Python.


#Challenges:
#Everytime I tried to stop or run my code, it would show the URL to a file, and finish with exit code 130 as well as other syntax errors.
#Eventually, I decided that I would leave the prompt as is with the code I wrote although the code would not fully run through since I didn't input values.
#When I started question 2 and tried to run my code, it would give me a SyntaxError.
#I didn't understand that I need to plug in the values when my code begins to run. I was stuck on just having "Enter weight in kilograms show" with nothing else.
#For the troubleshooting section of this assignment, I had to make a quick Google search to understand variables that work and do not work to better understand the answer I gave you.
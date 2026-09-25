#Part 1: Errors in Data vs. Errors in Code

#Situation 1: The program expects an integer but the user enters hello.
#Bad input or bug? BAD INPUT
#Reasoning: the program's instructions are right, but the user provides an invalid data type that cannot be processed

#Situation 2: The programmer writes prin() instead of print()
#Bad input or bug? BUG IN CODE
#Reasoning: This is a syntax error and invalid function

#Situation 3: The program divides by a value enter by the user, and the user enters 0.
#Bad input or bug? BAD INPUT
#Reasoning: You can divide, but cannot divide by 0.

#Part 2: Reading an Exception
#1. the int("") operation
#2. When the user presses enter without typing anything, an empty string is returned
#3.ValueError tells the programmer that it received a valid string but an invalid value
#4.No. Entering 0 would convert into an integer through int("0"), but in line 2, 1/0 would cause an error since you cannot divide by 0

#3. Complete a Basic try-except
#Entering 4:the string "4" is converted to integer 4. Output: "You entered: 4"
#Entering abc: the string "abc" is a ValueError. Output:"Invalid input. Please enter a valid integer."
#Entering an empty input: A ValueError. Output: "Invalid input. Please enter a valid integer."
try:
    value=int(input("Enter an integer:"))
    print("You entered:", value)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#Part 4: Trace try-except Control Flow
#Input: 2
#Lines/Branches executed: Prints: "A", "B", "C", "D"
#Lines skipped: both except blocks
#Exception: None

#Input: 0
#Lines/Branches executed: prints "A", "B", "Cannot divide by zero", "D"
#Lines skipped: print("C", except ValueError block
#Excpetion:ZeroDivisionError

#Input: hello
#Lines/Branches Executed: prints "A", "Invalid value", "D"
#Lines Skipped: Print("B"), result=10/value, print("C"), except ZeroDivisionError block
#Exception: ValueError

#print("C") doesn't execute when you divide by 0 because when result= 10/ value, value=0, a ZeroDivisionError occurs. Python stops the normal execution of the try block and goes to the except ZeroDivisionFunction block, thus skipping print("C") completely

#Part 5: Handle more than one Exception
try:
    num= int(input("Enter an integer:"))
    reciprocal=1/num
    print("The reciprocal of {num} is {reciprocal}".format(num=num,reciprocal=reciprocal))
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Invalid input. Zero does not have a reciprocal")

#Test 1: (3)
#Output: The reciprocal of 3 is 0.333333333333
#Result: Runs without triggering an except block

#Test 2: (0)
#Output: Invalid input. Zero does not have a reciprocal
#Result: 1/0 causes ZeroDivisionError, jumping to second except block.

#Test 3: (a)
#Output: Invalid input. Please enter a valid number.
#Result: Triggers a ValueError, jumping to first except block

#Test 4: ( )
#Output: Invalid input. Please enter a valid number.
#Result: Triggers ValueError, jumps to first except block

#Python evaluates except blocks from top to bottom. If an exception is inside a try block, Python searches that list for the first matching except block.

#Part 6: Common Python Exceptions

#Fragment A:
#   Exception: ValueError
#   Reason: int("hello") trys to convert letters into an integer, which is an invalid value for the int() function

#Fragment B:
#   Exception: ZeroDivisionError
#   Reason: result= 10% 0 uses % with a division of 0, which is not possible since you're unable to divide by 0

#Fragment C:
#   Exception: TypeError
#   Reason:1.5 uses a float(1.5) as a list index. Python lists cannot be floating-point numbers.

#Fragment D:
#   Exception: AttributeError
#   Reason: values.depend(3) attempts to use depend() ona list object. Lists don't have a .depend()

#Part 7: The Default Except Branch
#1. The final except branch is the last level to catch any exception that was not handled by the other except blocks
#2. Only if an exception is raised in the try block that doesn't match the ValueError or ZeroDivisionError.
#3. It has to appear last because Python processes exception blocks in order from top to bottom. Except at the end catches all the last errors
#4. Specific handlers find the cause of an error, allowing the program to provide messages that help a programmer take correct action to fix the issue.

#Part 8: Syntax Errors are Different
# SyntaxError
# There is a missing colon at the end of the if value > 0[:]
#Syntax Errors happen before the code runs, so try-except blocks can't prevent a SyntaxError from stopping execution. Syntax errors represent invalid code rules.

#Part 9: Test Every Execution Path
#Test Input A: 5
#Expected Path: if number > 0:
#Expected Result: "Positive"
#Actual Result: "Positive"
#Pass/Fail: Pass

#Test Input B: -2
#Expected Path: elif number<0:
#Expected Result: Negative
#Actual Result: Negative
#Pass/Fail: Pass

#Test Input C: 0
#Expected Path: else: branch
#Expected Result: Zero
#Actual Result: Zero
#Pass/Fail: Pass

#One successful test only proves that that specific integer works under the set conditions

#Part 10: Find the hidden bug
value= float(input("Enter a number:"))
if value > 0:
    print("Positive")
elif value < 0:
    print("Negative")
else:
    print("Zero")

#1. Yes, the program works for the test because entering 0 activates the else: branch, giving the output of zero
#2. elif value < 0: contains the bug
#3. Inserting a negative number will expose the bug
#4. This shows that code can contain bugs that could remain unknown if you only test some paths and not all.

#Part 11: Print Debugging
#1. Expected result: Total = 12.50 x 4 = 50.0
#2. Actual Result: Total: 16.5
#3.
def calculate_total(price, quanity):
    print(f"DEBUG: Function with price ={price}, quantity ={quanity}")
    total= price + quanity
    print(f"DEBUG: Total before returning={total}")
    return total
price= float(input("Price:"))
quantity= int(input("Quantity:"))
print(f"DEBUG: Inputs recieved; price ={price}, quantity ={quantity}")
result = calculate_total(price, quantity)
print("Total", result)
#4.
#4a.print at input conversion confirms that price and quantity are read and put into the right data points.
#4b.print at function entry confirms that values are passed into calculate_total() in the right order
#4c.print before return total shows that 16.5  is the math error

#5. Line 2 has the + operation instead of the * operation making the result show 16.50. To correct this, change signs

#7.
def calculate_total(price, quanity):
    total=price*quanity
    return total
price= float(input("Price:"))
quantity= int(input("Quantity:"))

result= calculate_total(price, quantity)
print("Total:", result)

#Part 12: Integrated Exception-Handling Program
try:
    number1= int(input("Enter a number:"))
    number2= int(input("Enter another number:"))
    result = number1 / number2
    print(f"The quotient is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Invalid input. Cannot divide by zero.")

#Test 1. Input 1- 8. Input 2- 4. Expected Path: try block only. Expected result: "The quotient is: 2.0". Actual Result: "The quotient is 2.0" PASS
#Test 2. Input 1- 8. Input 2- 0. Expected path: except ZeroDivisionError. Expected result: Invalid input. Cannot divide by zero. Actual result: "Invalid input. Cannot divide by zero." PASS
#Test 3. Input 1- 8. Input 2- x. Expected path: except ValueError. Expected Result: "Invalid input. Please enter a valid number." Actual result: "Invalid input. Please enter a valid number." PASS
#Test 4. Input 1. y. Input 2- x. Expected path: except ValueError. Expected result: "Invalid input. Please enter a valid number." Actual result: "Invalid inout. Please enter a valid number." PASS

#Analysis/Reflection
#1. Raising an exception is when an error is detected (entering a letter or dividing by zero). The program creates an exception object that contains into about the error.
#2. The remaining statements are skipped.
#3. Seperate handlers identify the specific error type for clear messages to be tailored to each error.
#4. Exception handling only prevents crashed when running and not incorrect math formulas. A program can run even if it has errors due to these bugs
#5.Code can contain syntax errors and never be discovered if they are in an elif or try block. Testing each path ensures that the code is error free
#6.Placing print() statements can reveal data types as code executes step-by-step

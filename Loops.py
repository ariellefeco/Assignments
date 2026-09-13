#1. While Loop
#a. Python code using a while loop to preform:
n0=int(input("Enter a positive number:"))
steps=0
while n0 !=1:
    if n0%2==0:
        n0=n0//2
    else:
        n0=3*n0+1
    print(n0)
    steps+=1
print(f"steps: {steps}")

#b. Infinite loops issue
#while True:
    #print("This runs forever...")
while True:
    user_input = input("Type 'stop' to exit:")
    if user_input. lower()=="stop":
        break

#c.
while True:
    number1=float(input("Enter a number:"))
    number2=float(input("Enter another number:"))

    op= input("Chose operation (+,-,*,/):")
    if op=="+":
        print("Answer:", number1+number2)
    elif op=="-":
        print("Answer:", number1-number2)
    elif op=="*":
        print("Answer:", number1*number2)
    elif op=="/":
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            print("Answer:", number1/number2)
    else:
        print("Invalid operation")
    again=input("Do you want to continue (y/n)?")
    if again == "n":
        print("Have a good day!")
        break
    elif again == "y":
        continue

#2. For loops that count character count
text= input("Enter a sentence:")
total_alphabets = 0
letter_counts={}
for character in text:
    if character.isalpha():
        total_alphabets+=1
        lower_character=character.lower()

        if lower_character in letter_counts:
            letter_counts[lower_character]+=1
        else:
            letter_counts[lower_character]=1
print(f"Total number of alphabets: {total_alphabets}")
print(f"Total number of distinct alphabets are: {len(letter_counts)}")

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")


#Challenges
#After creating the infinite loop, my computer almost crashed. I also could no figure out how to run the next part of my code after that.
#While making the loops in question 1C, I had some mistakes in my code, such as forgetting to write 'while true' and 'break/continue' which was a challenge to find and resolve.
#I had trouble with the indentation of my code, making the computer think that my 'continue/break' were outside of the loop
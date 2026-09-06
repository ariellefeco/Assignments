print("1. Literals")
print(5+2-2)
#5
print(5/2)
#2.5
print(6//2) # // integer division
#3
print(2.*3)
#6.0
print(2<4)
#True
print(2>=2)
#True
print("Hello"+"World")
# Hello World
print("bla"*3)
# bla bla bla
print(2*3**3)
#54
print(5*25//13+100/2%13//2)
#14
print(2*3%5)
#1
print((2%-4), (2%4), (2**3**2))
#-2 2 512

print("2. Data Type")
print(type("Hello"))
#Hello -> <class 'str'>
print(type(str(1)+"2"))
#3 -> <class 'str'>
print(type(1.))
#1.0 -> <class 'float'>
print(type('A'))
#A -> <class 'str'>
print(type(500))
#500 -> <class 'int'>
print(type(True))
#True -> <class 'bool'>
print(type("False"))
#False -> <class 'str'>

print("3. Operator Precedence")
print("Arithmetic Expression")
print("Example Equation: 5 + 3 * 2 * * 3/(4-2)")
print("1.Parentheses: (4-2)=2 ... Expression becomes: 5 + 3 * 2 * * 3/2")
print("2.Exponents: 2 * * 3 = 8 ... Expression becomes: 5 + 3 * 8/2")
print("3.Multiplication/Division:(*./) from Left to Right ... Expression becomes: 3*8=24 & 24/2= 12")
print("4.Addition: 12+5=17")
print("Final Answer: 17")

# Challenges I Faced
#I wrote "type" for the second question instead of "print(type("Hello"))" and the program could not read the commands.
#For the answers on question two, I didn't realize that type meant the type of format of the code.
#Pycharm kept flagging my code with warnings. After a quick Google search, I learned that it likely means I am preforming a redundant step or that the code I wrote won't actually achieve a useful result.
#I kept getting an TypeError code for 'int' and 'str' in some of the code. To fix this I changed the '1' in 'print(type(1+"2")) to "print(type(str(1)+"2")) in line 30.
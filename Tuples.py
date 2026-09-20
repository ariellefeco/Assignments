#1. Exercising Tuples
#1a.
#my_tuple = (input("Enter an input:"),
#            input("Enter another input:"),
#            input("Enter another input:"),
#            input("Enter another input:"),
#            input("Enter another input:"))
#print(my_tuple)

#1b.
#single_element_tuple = ("Hi",)

#1c.
#my_tuple =(1,2,3,4,3,2,1,2,3,5,4,3,2,1)
#for number in set(my_tuple):
#        print(f"{number} appears {my_tuple.count(number)} time(s)")

#1d.
#my_tuple_c=(1,2,3,4,3,2,1,2,3,5,4,3,2,1)
#my_tuple_d=my_tuple + my_tuple
#Proof:
#print("length of c:" len(my_tuple_c)
#print("length of d:" len(my_tuple_d)

#1e. WITHOUT USING PYTHON:
#x.append(1) is illegal for the tuple because it tries to add to the end of the program sequence. Tuples cannot change after created, so they don't support ".append()"
#x[1]="hello" is illegal because it is trying to alter x=(1,2,3,4). This doesn't work because tuples cannot be changed.
#del x[2] is illegal because it is trying to delete '2' from the original tuple sequence. Single values can't be removed from the tuple.

#2. Packing and Unpacking Tuples

#2a. Each variable is an integer. The data type is int

#2b/c.
x=(1,2,[3,4])
a,b,*c=x
print("a=", a)
print("b=",b)
print("c=",c)

#3.Memory Management
#Lists and tuples store memory addresses of integer objects over storing actual values. Python resues the same address when the same numbers appear.
my_x =[100,200,300,400]
my_y =(200,300,400,500)
print("Index", "my_x_address","my_y_address", sep=(" | "))
for i in range(len(my_x)):
    print(i,id(my_x[i]),id(my_y[i]),sep=(" | "))

#Challenges:
#It was hard to conceptually understand why Python reuses memory addresses (if()) for identical numbers. I had to watch some Youtube videos to better understand it.
#Remembering that tuples can't be changed was challenging for me since I kept getting TypeError results
#Learning how to use an asterisk was challenging. I needed to watch videos to supplement my understanding.
#1a.
def convert_fuel_efficiency(direction,*values):
    factor=2.35215
    results=[]
#direction 1: KPLP to MPG
    if direction== "1":
        for val in values:
            cleaned_val=str(val).replace(".","",1)
            if cleaned_val.isdigit():
                num=float(val)
                mpg=num * factor
                results.append(str(round(mpg,2))+"mpg")
            else:
             print("'"+str(val) + "'is an invalid input." )
#direction 2: mpg to kpl
    elif direction=="2":
        for val in values:
            cleaned_val=str(val).replace(".","",1)
            if cleaned_val.isdigit():
                num=float(val)
                kpl=num/factor
                results.append(str(round(kpl,2))+"kpl")
            else:
                print(""'"+str(val)+"is an invalid input.' )
        else:
            print("Error. Please choose 1 or 2.")
        return results

#1b.
def print_in_reverse(*args):
    for item in reversed(args):
        print(item)
print("Test 1")
print_in_reverse(1,2,3,4,5)
print("Test 2")
print_in_reverse("Hi","how","are","you?")

#1c.
#Risky
def change_risky(a_list,a_dict):
    a_list.append(99)
    a_dict["status"]="changed"
#Safe
def change_safe(a_list,a_dict):
   c_list=a_list.copy()
   c_dict=a_dict.copy()
   c_list.append(100)
   c_dict["status"]="new"
   return c_list,c_dict
#Test Risky
my_list=[1,2,3,4,5]
my_dict={"a":1}
change_risky(my_list,my_dict)
print("Risky outcome:", my_list, my_dict)
#Test Safe
num_list=[1,2]
num_dict={"a":1,"b":2}
new_l, new_d= change_safe(num_list,num_dict)
print("Original list:",num_list, num_dict)
print("Updated copies", new_l, new_d)

#1d.
#funct_1(), x is 5
#funct_2(), x is 2

#2. Troubleshooting
def my_func(a,b,*c):
    print(c)
my_func(1,2,3,4,5,6)
#1 goes to a, 2 goes to b, the rest of the values are outputs without names

#this function prints 10 because when my_func_global() runs, Python notes x=100 and writes that in the local notebook instead. This is why when the function stops running, the global notebook still says x=10

#Challenges
#I struggled with remembering that global vs. local variables assigned in a fucntion stay local to that certain function. I also had troubl determining where to place the global keyword.
#It was challenging to distingush between *args and **kwargs
#It was hard to conceptually understand the use of .copy() and how it kept my orignial variables unchanged/safe
#Had some syntax errors caused by incorrect functions
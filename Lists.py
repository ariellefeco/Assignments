#1. Lists
#a.
import copy

my_list= list(range(100))
print("Data type of my_list:", type(my_list))
my_list.append(100)
my_list.reverse()
my_list.pop()
my_list.sort()
print("Modified my_list length:", len(my_list))

#b.
sample_list=[1,2,3,4,5,6,7,8,9,10]
reordered_list=sample_list[-3:] + sample_list[:-3]
print("reordered list:", reordered_list)

#c.
result_c=len([[1,2]] * 3)
print("Result of c:", result_c)

#d.
my_list_ten=[10,20,"apple",10, "banner", "apple",30,40,50,10]
my_list_ten_mem=[id(item) for item in my_list_ten]
print(my_list_ten_mem)

#e.
del my_list_ten

#f.
my_new_list=[10,20,"apple",10,"banner","apple",30,40,50,10]
my_new_list_mem=[id(item) for item in my_new_list]
print(my_new_list_mem)

#g.
x=[[1,2,3],[4,5,6],[7,8,9]]
y=copy.deepcopy(x)

#h.Yes, you can include multiple 'for' clauses and 'if' statements

#i.
text="To be, or not to be, this is the question"
space_count= sum(1 for item in text if item==" ")
print("Number of spaces:",space_count)

#j.
sample_list =[10,20,30]
sample_list.append(40)
sample_list.insert(1,40)
sample_list.remove(10)
popped_item=sample_list.pop()
print("List before clearing:", sample_list)
sample_list.clear()
print("Final list:",sample_list)

#Challenges
#I accidentally has an extra bracket in line 36 that threw off the copy-deepcopy().
#I also wrote my_list instead of type(my_list) which created confusion in my code
#During part i, I used an empty string with no space in between, resulting in zero matches found by Python
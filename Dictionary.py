#1. Create and Access Dictionary
#1a.
my_dict={
    "red":"color",
    "water bottle":"object",
    "cheese":"food",
    "winter":"season",
    "cat":"animal",
    "dog":"animal",
    "motorcycle":"vehicle",
    "piano": "instrument",
    "truck": "vehicle",
    "python":"language"
}

#1b.
my_user_dict={}
keep_going="Y"
while keep_going=="Y" or keep_going=="y":
    ssn=input("Enter your ssn: ")
    name=input("Enter your name: ")
    my_user_dict[ssn]=name
    keep_going=input("Would you like to continue or stop? (Y/N): ")
key_count=0
for key in my_user_dict:
    key_count= key_count+1
print("User Dictionary:", my_user_dict)
print("Number of keys created:", key_count)

#1c.
tuple_list=[
    ('Name','Sarah Connor'),
    ('Date of birth','1 Jan 1980'),
    ('Address','1000 Black Mountain Drive,',92126),
    ('Name','Jim Hawkins')]
my_dict={}
for item in tuple_list:
    item_count=0
    for element in item:
        item_count= item_count+1
    if item_count !=2:
        print("Invalid key-value pair found:", item)
        key=input("Please enter a valid key: ")
        val= input("Please enter a valid value: ")
    else:
        key=item[0]
        val=item[1]
    while key in my_dict:
        print("The key '"+key+"' is already present in the dictionary.")
        key=input("Please enter a new key: ")
    my_dict[key]=val
print("Final Dictionary:")
print(my_dict)

#1d.
tuple_list=[
    ('Name','Sarah Connor'),
    ('Date of birth','1 Jan 1980'),
    ('Address','1000 Black Mountain Drive,',92126),
    ('Name','Jim Hawkins')
]
my_dict={}
for item in tuple_list:
    key=item[0]
    value=item[1]
    while key in my_dict:
        print("The key '"+key+"' is already present in the dictionary.")
        key=input("Please enter a new key for value ' "+key+"': ")
    my_dict[key]=value
print("Final Dictionary:")
print(my_dict)

#1e.
text="The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia. It has a powerful, muscular body with a large head and paws, a long tail and orange fur with black, mostly vertical stripes. It is traditionally classified into nine recent subspecies, though some recognise only two subspecies, mainland Asian tigers and the island tigers of the Sundra Islands."
cleaned_text= text.replace(",","").replace(".","").replace("(","").replace(")","")
word_list=cleaned_text.split()
word_counts={}
for word in word_list:
    if word in word_counts:
        word_counts[word]= word_counts[word]+1
    else:
        word_counts[word]=1
print("Word Counts Dictionary:")
print(word_counts)

#2. Troubleshooting
#2a.
d_orig={123:"Coconut"}
d_copy=d_orig
d_copy[123]="Apple"
print("d_orig:", d_orig)
print("d_copy:", d_copy)

#2b.
d_orig={123:"Coconut"}
d_copy=d_orig.copy()
d_copy[123]="Apple"
print("d_orig:",d_orig)
print("d_copy:",d_copy)

#2c.
#my_list=[1,2,3]
#my_dict={my_list:"Error"}

#Challenges:
#When creating my dictionary, I forgot to separate the elements with commas, giving me a plethora of issues that I didn't know to resolve
#I had trouble with 1c. I was not sure how to properly show a valid key pair. I thought that the tuple list for 1d. was meant for 1c.
#Had trouble with appreviating and keeping whole words. I used val and value in the same code, intending for them to be the same. It caused issues.
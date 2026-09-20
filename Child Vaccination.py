#1. insert function/data structure
#Define Patient
patient={}
#Define function
def insert(patient_dict):
    record_num=len(patient_dict)+1
    first_name= input("Enter the patient's first name:")
    last_name= input("Enter the patient's last name:")
    vaccine_month=int(input("Enter the birth month when the vaccine was administered (1-12):"))
    patient_dict[record_num]={
        "First_name":first_name,
        "Last_name":last_name,
        "Vaccine_month":vaccine_month
    }
    return patient_dict
#What the function shows after running
insert(patient)
print(patient)

#3. Verification steps
#add the first patient
print("Add A Patient")
insert(patient)
print("Patient dictionary after first entry:")
print(patient)
#add the second patient
print("Add Second Patient")
insert(patient)
#verify that records work
print("Final Patient Dictionary")
print(patient)

#Challenges
#For questions 1 and 2 I had some trouble with the def and figuring out how to make the code show when being run
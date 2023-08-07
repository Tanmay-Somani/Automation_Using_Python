elem=int(input("enter the number of elements you want to add in a list"))
lise=[]
emp_str=""
for i in range(elem):
    element_=input("Enter the elements ")
    lise.append(element_)
for i in lise:
    emp_str+=i
    emp_str+=", "
print(emp_str)

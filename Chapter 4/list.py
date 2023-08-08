elem=int(input("enter the number of elements you want to add in a list"))
lise=[]
emp_str=""
for i in range(elem):
    element_=input("Enter the elements ")
    lise.append(element_)
for i in range(len(lise)-1):
    emp_str+=lise[i]
    emp_str+=", "
emp_str+="and "+ lise[len(lise)-1] #lise[3]
print(emp_str)

Birthdays={}
loop=int(input("Enter the number of pairs in the Birthday") )
for i in range(loop):
    key=input("enter the name: ")
    value=input("enter the Birthday: ")
    Birthdays[key]=value

while True:
    name=input("Enter a name: ")
    if name==" ":
        break 

if name in Birthdays:
    print(Birthdays[name]+' is the birthday of'+name)
else:
    print("I do not have birthday information for"+name)
    print("what is their birthday on")
    bday=input()
    Birthdays[name]=bday
    print("Birthday database updated. ")
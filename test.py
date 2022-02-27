import random

num1=random.randint(1,6)
num2=random.randint(1,6)
print("I have just rolled dice, the numbers produced are:",num1,num2)
a=str(input("if you want to add the 2 numbers you must enter add, if you want to subtract the 2 numbers you must enter sub : ")
)
if a=="add":
    print(num1+num2)
if a=="sub":
    print(num1-num2)
if a!="sub"and a!="add":
    print("I do not understand your response")

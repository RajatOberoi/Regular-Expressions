#Q.1- Write a python code to find a valid email address from a text.

import re
a=input("type your text")
count=0
b=re.finditer("[a-zA-z][a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)",a)
for i in b:
    count+=1
    print(i.group(),"is a valid id")
if count==0:
    print("not a valid id")

#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )

a=input("enter no")
count=0
b=re.finditer("[6-9][0-9]{9}",a)
for i in b:
    count+=1
    print(i.group(),"is a valid number")
if count==0:
    print("not a valid number")
    

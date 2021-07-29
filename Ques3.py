array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
array1=[]
e=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for j in range(0,e):
    q=input("ENTER THE ELEMENT:")
    array1.append(q)
print(array1)
array.extend(array1)
array2=[]
y=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for k in range(0,y):
    r=input("ENTER THE ELEMENT:")
    array2.append(r)
print(array2)
array.extend(array2)
array3=[]
b=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for l in range(0,b):
    s=input("ENTER THE ELEMENT:")
    array3.append(s)
print(array3)
array.extend(array3)
print(array)
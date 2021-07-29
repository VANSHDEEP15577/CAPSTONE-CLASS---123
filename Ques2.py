array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
po=int(input("ENTER THE POSITION WHERE YOU WANT TO DELETE:"))
array.pop(po-1)
print(array)

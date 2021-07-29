array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
for j in range(0,3):
    pos1=int(input("ENTER THE POSITION WHERE YOU WANT TO ADD:"))
    a=input("ENTER THE ELEMENT YOU WANT TO ADD:")
    array.insert(pos1-1,a)
print(array)


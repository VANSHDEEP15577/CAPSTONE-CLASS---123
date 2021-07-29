list=[]
c=0
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=int(input("ENTER THE ELEMENT:"))
    list.append(p)
y=int(input("ENTER THE NO. YOU WANT TO FIND:"))
res=-1
for j in range(0,w):
    if list[j] == y:
        res=j
    else:
        res=-1
if res == -1:
    print("THE NO. IS NOT IN THE ARRAY")
else:
    print("THE NO. IS IN THE ARRAY")
c=list.count(y)
print("NO. OF OCCURRENCES OF ",y," IS:",c)
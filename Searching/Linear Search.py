n=int(input("Enter the number of elements you want to enter: "))
l=[]
f=0
print("Enter the elements:")
for i in range(n):
    l.append(int(input()))
print("Enter the element you want to search:")
key=int(input())
for i in range(n):
    if key==l[i]:
        pos=i
        f=1
        break
if f==1:
    print("Element found at position: ",(i+1))
else:
    print("Sorry, No such element found")
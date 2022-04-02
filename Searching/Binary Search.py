n=int(input("Enter the number of elements you want to enter: "))
l=[]
f=0
print("Enter the elements in sorted manner:")
for i in range(n):
    l.append(int(input()))
print("Enter the element you want to search:")
key=int(input())
low=0
high=n-1
while low<=high:
    mid=(high+low)//2
    if key==l[mid]:
        pos=mid+1
        f=1
        break
    elif key>l[mid]:
        low=mid+1
    else:
        high=mid-1
if f==0:
    print("Sorry, No such element found")
else:
    print("Element found at position: ",pos)
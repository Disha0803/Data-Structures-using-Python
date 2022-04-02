n=int(input("Enter the number of elements you want to enter: "))
l=[]
print("Enter the elements:")
for i in range(n):
    l.append(int(input()))
for i in range(1,n):
    temp=l[i]
    j=i-1
    while j>=0 and temp<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=temp
print("The sorted list is:")
for i in range(n):
    print(l[i],end=' ')
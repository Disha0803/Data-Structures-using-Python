n=int(input("Enter the number of elements you want to enter: "))
l=[]
print("Enter the elements:")
for i in range(n):
    l.append(int(input()))
for i in range(n-1):
    for j in range(n-1-i):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print("The sorted list is:")
for i in range(n):
    print(l[i],end=' ')
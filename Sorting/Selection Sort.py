n=int(input("Enter the number of elements you want to enter: "))
l=[]
print("Enter the elements:")
for i in range(n):
    l.append(int(input()))
print("Before Sorting:")
for i in range(n):
    print(l[i],end=' ')
for i in range(n):
    # j=i+1
    for j in range(i+1,n):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("\nAfter Sorting:")
for i in range(n):
    print(l[i],end=' ')
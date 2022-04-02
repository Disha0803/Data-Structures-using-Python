def create():
    stack=[]
    return stack
def check(stack):
    if len(stack)==0:
        return 0
    else:
        return 1
def push(stack,item):
    stack.append(item)
    print("Pushed ",item)
def pop(stack):
    if (check(stack)==0):
        return "Empty Stack"
    return stack.pop()

n=int(input("How many elements you want to enter into the stack: "))
print("Enter the elemnts:")
s=create()
for i in range(n):
    push(s,input())
ch=0
while ch!=4:
    print("Do you want to continue?")
    print("Choose according to your choice:\n1-->push\n2-->pop\n3-->display stack\n4-->exit")
    ch=int(input())
    if ch==1:
        print("Enter the element to push:")
        push(s,input())
    elif ch==2:
        pop(s)
    elif ch==3:
        print(s)
    elif ch==4:
        break
    else:
        print("Wrong choice")
    


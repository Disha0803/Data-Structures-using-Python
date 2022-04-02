def create():
    q=[]
    return q
def check(q):
    if len(q)==0:
        return 0
    else:
        return 1
def enqueue(q,item):
    q.append(item)
    print("Enqueued ",item)
def dequeue(q):
    if (check(q)==0):
        return "Empty q"
    return q.pop(0)

n=int(input("How many elements you want to enter into the queue: "))
print("Enter the elemnts:")
s=create()
for i in range(n):
    enqueue(s,input())
ch=0
while ch!=4:
    print("Do you want to continue?")
    print("Choose according to your choice:\n1-->enqueue\n2-->dequeue\n3-->display queue\n4-->exit")
    ch=int(input())
    if ch==1:
        print("Enter the element to enqueue:")
        enqueue(s,input())
    elif ch==2:
        dequeue(s)
    elif ch==3:
        print(s)
    elif ch==4:
        break
    else:
        print("Wrong choice")
    


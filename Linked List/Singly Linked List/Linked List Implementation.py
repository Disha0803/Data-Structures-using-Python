class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_List:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Node is Empty")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_Begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head=self.head.ref

    def delete_End(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_by_value(self,x):
        if self.head is None:
            print("Can't DElete coz its empty")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref

r=Linked_List()
print("You can operate on Linked List here")
r.display()
ch=0
while ch!=9:
    print("Do you want to continue?")
    print("Choose according to your choice:\n1-->Display List\n2-->Add at Beginning\n3-->Add at End\n4-->Add After a Value\n5-->Add Before a Value\n6-->Delete At Beginning\n7-->Delete At End\n8-->Delete By Value\n9-->Exit")
    ch=int(input())
    if ch==1:
        r.display()
    elif ch==2:
        x=int(input("Enter a value to add at the beginning: "))
        r.add_begin(x)
    elif ch==3:
        x=int(input("Enter a value to add at the End: "))
        r.add_end(x)
    elif ch==4:
        d=int(input("Enter the data after which you want to add: "))
        x=int(input("Enter the value you want to add: "))
        r.add_after(x,d)
    elif ch==5:
        d=int(input("Enter the data before which you want to add: "))
        x=int(input("Enter the value you want to add: "))
        r.add_before(x,d)
    elif ch==6:
        r.delete_Begin()
    elif ch==7:
        r.delete_End()
    elif ch==8:
        x=int(input("Enter the value you want to delete: "))
        r.delete_by_value(x)
    elif ch==9:
        exit()
    else:
        print("Invalid Input")




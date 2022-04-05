class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class Doubly_Linked_List:
    def __init__(self):
        self.head=None
    def fdisplay(self):
        if self.head is None:
            print("Linked List is Empty!!!")
        else:
            n=self.head
            while n is not None:
                print(n.data," --> ",end=" ")
                n=n.nref
    def rdisplay(self):
        print()
        if self.head is None:
            print("Empty Linked List!!!")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data," <-- ",end=" ")
                n=n.pref

    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is not Empty!!!")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,x):
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("No such Node exists")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
    
    def add_before(self,data,x):
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("No such Node exists")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
    def delete_begin(self):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.nref is None:
            self.head=None
            print("Linked List is empty after deletion")
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_end(self):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.nref is None:
            self.head=None
            print("Linked List is empty after deletion")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_by_value(self,x):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head is None:
            if x==self.head.data:
                self.head=None
            else:
                print("No such value exists in the list")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("No such value exists")


r=Doubly_Linked_List()
print("You can operate on Doubly Linked List here")
r.fdisplay()
print("Do you want to add data in the Doubly Linked List? [y|n]")
c1=input()
if c1=='y':
    data=int(input("Enter the value you want to add: "))
    r.add_empty(data)
    r.fdisplay()
ch=0
while ch!=9:
    print("\nDo you want to continue?")
    print("Choose according to your choice:\n1-->Display List\n2-->Add at Beginning\n3-->Add at End\n4-->Add After a Value\n5-->Add Before a Value\n6-->Delete At Beginning\n7-->Delete At End\n8-->Delete By Value\n9-->Exit")
    ch=int(input())
    if ch==1:
        c2=input("Do you want to see the list in forward and reverse order? [f|r]")
        if c2=='f':
            r.fdisplay()
        elif c2=='r':
            r.rdisplay()
        else:
            print("Invalid Input!!!")  
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
        r.delete_begin()
    elif ch==7:
        r.delete_end()
    elif ch==8:
        x=int(input("Enter the value you want to delete: "))
        r.delete_by_value(x)
    elif ch==9:
        exit()
    else:
        print("Invalid Input")




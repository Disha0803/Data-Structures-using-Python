

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
                n=n.ref
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
r.add_empty(10)
r.add_end(20)
r.add_begin(0)
r.add_after(30,20)
r.add_before(25.5,30)
r.add_after(35.5,30)
r.add_before(-0.5,0)
r.delete_begin()
r.delete_end()
r.delete_by_value(20)
r.fdisplay()
r.rdisplay()
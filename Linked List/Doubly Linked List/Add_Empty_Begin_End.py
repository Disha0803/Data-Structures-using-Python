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

r=Doubly_Linked_List()
r.add_empty(10)
r.add_end(20)
r.add_begin(0)
r.fdisplay()
r.rdisplay()
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
            while n.nref is not None:
                print(n.data," --> ",end=" ")
                n=n.nref
    def rdisplay(self):
        print()
        if self.head is None:
            print("Empty Linked List!!!")
        else:
            n=self.head
            while n is not None:
                n=n.nref
            while n.pref is not None:
                print(n.data," --> ",end=" ")
                n=n.pref
r=Doubly_Linked_List()
r.fdisplay()
r.rdisplay()
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_List:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
r=Linked_List()
r.display()
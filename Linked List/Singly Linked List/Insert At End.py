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
                print(n.data,"--->", end=" ")
                n=n.ref
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
r=Linked_List()
r.add_end(100)
r.add_end(500)
r.display()
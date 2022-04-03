
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_List:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
r=Linked_List()
r.add_begin(20)
r.display()
class MyListNode:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self,val):
        self.head = MyListNode(val)

    def head_insert(self,val):
        new_node = MyListNode(val)
        new_node.next = self.head
        self.head = new_node

    def tail_insert(self,val):
        new_node = MyListNode(val)
        cur_node = self.head
        while(cur_node.next != None):
            end_node = cur_node
            cur_node=cur_node.next
        end_node.next=new_node


    def print_ll(self):
        if self.head == None :
            return
        
        print("< Head >-<",self.head.val,end=" >-")
        cur_node = self.head.next
        while(cur_node != None):
            print("<",cur_node.val,end=" >-")
            cur_node=cur_node.next
        print("< tail >")


        
myll = Linkedlist(2)
myll.print_ll()

myll.head_insert(3)
myll.print_ll()

myll.head_insert(7)
myll.print_ll()

myll.tail_insert(15)
myll.print_ll()


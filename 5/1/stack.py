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
    def del_head(self):
        if self.head==None:
            return
        else:
            self.head=self.head.next
            


    def print_ll(self):
        if self.head == None :
            return
        
        print("< Head >-<",self.head.val,end=" >-")
        cur_node = self.head.next
        while(cur_node != None):
            print("<",cur_node.val,end=" >-")
            cur_node=cur_node.next
        print("< tail >")




class Stack:
    

    def __init__(self,val = 0):
        self.stack = Linkedlist(val)
        self.size = 1
        
    
   

    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return self.size == 0


    def push(self, val: int):
        """入栈"""
        self.stack.head_insert(val)
        self.size += 1



     

    def pop(self) -> int:
        """出栈"""
        if self.stack.head == None : return None
        return_value = self.stack.head.val
        self.stack.del_head()
        self.size -=1
        return return_value



    def peek(self) -> int:
        """访问栈顶元素"""
        return self.stack.head.val

    def to_list(self) -> list[int]:
        """转化为列表用于打印"""
        if self.stack.head == None : return None
        list=[self.stack.head.val]
        cur =self.stack.head.next
        while(cur != None):
            list.append(cur.val) 
            cur = cur.next

        return list
    
s = Stack(2)
print(s.to_list())
s.push(3)
print(s.to_list())
s.push(4)
print(s.to_list())
print(s.size)
s.pop()
print(s.to_list())
print(s.peek())
s.pop()
s.pop()
s.pop()
print(s.to_list())



   
    
  
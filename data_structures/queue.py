## Queue - Double Linkedlist based
# - Insert element to queue - enqueue
# - Delete element form queue - dequeue



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.end = None
        
    def enqueue(self,data):
        nod = Node(data)
        if self.head == None:
            self.head = nod
            self.end = nod
        else:
            self.end.next = nod
            self.end = self.end.next
            
    def dequeue(self):
        if self.head is None:
            print('Queue is empty')
        else:
            print(f'Delete element from queue {self.head.data}')
            self.head = self.head.next
            
    def print_queue(self):
        if self.head is None:
            print('Queue is empty')
        curr = self.head
        while(True):
            if curr is None:
                break
            print(curr.data, end=' ')
            curr = curr.next
            
                
        
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.print_queue()
print(end='\n')
#------------------------------
q.dequeue()
q.print_queue()
print(end='\n')

q.dequeue()
q.print_queue()
print(end='\n')

q.dequeue()
q.print_queue()
print(end='\n')

# q.dequeue()

            
            
            
        
    
    
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class LinkedList:
    
    def __init__(self,first_node=None):
        self.head = first_node
        
    def add_node_front(self, value):
        if value is None:
            return
        node = Node(value)
        node.next = self.head
        self.head = node
                
    def print_list(self):
        current_node = self.head
        while current_node:
            print('node :> ', current_node.data)
            current_node = current_node.next
            
    def add_node_end(self, value):
        if self.head is None:
            self.head = Node(value)
            return
            
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next   
        current_node.next = Node(value)

            
    def search_element(self,value):
        if self.head is None:
            return
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
        return False
        
    
    def delete_element(self,value):
        if self.head is None:
            return
        
        if self.head.data is value:
            self.head = self.head.next
            print(f'Element : > deleted : {value}')
            return
            
        current_node = self.head
        while current_node.next:
            if current_node.next.data is value:
                current_node.next = current_node.next.next
                break
            else:
                current_node = current_node.next
                
                
                
            
            
        
            
        
        
        


# linked_list = LinkedList()
# linked_list.add_node_front(1)
# linked_list.add_node_front(2)
# linked_list.add_node_front(3)
# linked_list.add_node_front(4)
# linked_list.add_node_front(5)
# linked_list.print_list()


linked_list = LinkedList()
linked_list.add_node_end(1)
linked_list.add_node_end(2)
linked_list.add_node_end(3)
linked_list.add_node_end(4)
linked_list.add_node_end(5)
linked_list.print_list()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

linked_list.delete_element(2)
linked_list.print_list()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

linked_list.delete_element(1)
linked_list.print_list()
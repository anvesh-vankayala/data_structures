## Stack:
#    - Stack creation
#    - Pushing elements to stack
#    - Pop elements from stack, removes the last element inserted in stack.


class Stack:
    
    def __init__(self,size) -> None:
        
        self.arr = [None] * size
        self.idx = -1

    def push(self,ele):
        if self.idx == len(self.arr)-1:
            print('Stack is full')
        else:
            self.idx += 1
            self.arr[self.idx] = ele
    
    def pop(self):
        if self.idx == -1:
            print('Stack is empty')
        else:
            print(f'Removing the the element {self.arr[self.idx]}' )
            self.arr[self.idx] = None
            self.idx -= 1
            
            
stck = Stack(3)
stck.push(3)
stck.push(2)
stck.push(1)

print(f'After the 3 pushes :> {stck.arr}')

stck.pop()

print(f'After the 1st pop :> {stck.arr}')

stck.pop()

print(f'After the 2nd pop :> {stck.arr}')

stck.pop()

print(f'After the 3rd pop :> {stck.arr}')

stck.pop()

print(f'After the 4th pop :> {stck.arr}')

 
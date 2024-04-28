class Stack:
    def __init__(self):
        self.items = [] # this list will store the stack elements
    
    def push(self, item): # the push method adds an item to the top of the stack
        self.items.append(item) # implements a new item to the end of the array
    
    def pop(self): # the pop method removes and returns the top item of the stack
        if self.isEmpty():
            return None # return none if the stack is empty
        else:
            return self.items.pop()
    
    def peek(self): # this method retunrs the top item of the stack without removing it
        if self.isEmpty():
            return None
        else:
            return self.items[-1] # return the last item 
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def printStack(self):
        for item in self.items:
            print(item)


if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    print('hello world')
    
    list_of_fruits = [
        'apple', 
        'watermelon', 
        'banana', 
        'grapes', 
        'coconut',
        'kiwi',
        'mango',
        ]
    
    for fruit in list_of_fruits:
        stack.push(fruit)
    
    stack.printStack()
    print('-----------')
    stack.pop()
    stack.printStack()
    
    print('-----------')
    stack.push('orange')
    print(stack.peek())
    

# Implement a Stack data structure using a Python list. Create methods for push (add), pop (remove), and peek (view top element).

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        print(self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", end=" ")
s.display()

print("Top Element:", s.peek())
print("Popped Element:", s.pop())

print("Updated Stack:", end=" ")
s.display()

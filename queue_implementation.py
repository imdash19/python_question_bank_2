# Implement a Queue data structure using collections.deque. Create methods for enqueue (add to back) and dequeue (remove from front).

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.popleft()

    def display(self):
        print(list(self.queue))


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", end=" ")
q.display()

print("Dequeued Element:", q.dequeue())

print("Updated Queue:", end=" ")
q.display()

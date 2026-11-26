# Create a basic Node class and a LinkedList class. Implement a method to append a new node to the end of the list and a method to display the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


linked_list = LinkedList()

numbers = list(map(int, input().split()))

for num in numbers:
    linked_list.append(num)

linked_list.display()

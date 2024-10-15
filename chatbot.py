import time

# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self):
        if self.head:
            self.head = self.head.next

    def access(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return None

# Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

# Queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

# Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self):
        if self.head:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head = self.head.next

    def access(self, index):
        current = self.head
        count = 0
        if self.head:
            while True:
                if count == index:
                    return current.data
                current = current.next
                count += 1
                if current == self.head:
                    break
        return None

# Doubly Linked List
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def access(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return None

# Timing for LinkedList
ll_small = LinkedList()
ll_large = LinkedList()

start = time.time()
for i in range(3):
    ll_small.insert(i)
end = time.time()
print(f"Time to insert into small Linked List: {end - start:.8f} seconds")

start = time.time()
for i in range(10000):
    ll_large.insert(i)
end = time.time()
print(f"Time to insert into large Linked List: {end - start:.8f} seconds")

start = time.time()
ll_small.access(1)
end = time.time()
print(f"Time to access small Linked List: {end - start:.8f} seconds")

start = time.time()
ll_large.access(9999)
end = time.time()
print(f"Time to access large Linked List: {end - start:.8f} seconds")

# Timing for Stack
stack_small = Stack()
stack_large = Stack()

start = time.time()
for i in range(3):
    stack_small.push(i)
end = time.time()
print(f"Time to push into small Stack: {end - start:.8f} seconds")

start = time.time()
for i in range(10000):
    stack_large.push(i)
end = time.time()
print(f"Time to push into large Stack: {end - start:.8f} seconds")

start = time.time()
stack_small.peek()
end = time.time()
print(f"Time to peek small Stack: {end - start:.8f} seconds")

start = time.time()
stack_large.peek()
end = time.time()
print(f"Time to peek large Stack: {end - start:.8f} seconds")

# Timing for Queue
queue_small = Queue()
queue_large = Queue()

start = time.time()
for i in range(3):
    queue_small.enqueue(i)
end = time.time()
print(f"Time to enqueue into small Queue: {end - start:.8f} seconds")

start = time.time()
for i in range(10000):
    queue_large.enqueue(i)
end = time.time()
print(f"Time to enqueue into large Queue: {end - start:.8f} seconds")

start = time.time()
queue_small.dequeue()
end = time.time()
print(f"Time to dequeue from small Queue: {end - start:.8f} seconds")

start = time.time()
queue_large.dequeue()
end = time.time()
print(f"Time to dequeue from large Queue: {end - start:.8f} seconds")

# Timing for Circular Linked List
circular_ll_small = CircularLinkedList()
circular_ll_large = CircularLinkedList()

start = time.time()
for i in range(3):
    circular_ll_small.insert(i)
end = time.time()
print(f"Time to insert into small Circular Linked List: {end - start:.8f} seconds")

start = time.time()
for i in range(10000):
    circular_ll_large.insert(i)
end = time.time()
print(f"Time to insert into large Circular Linked List: {end - start:.8f} seconds")

start = time.time()
circular_ll_small.access(1)
end = time.time()
print(f"Time to access small Circular Linked List: {end - start:.8f} seconds")

start = time.time()
circular_ll_large.access(9999)
end = time.time()
print(f"Time to access large Circular Linked List: {end - start:.8f} seconds")

# Timing for Doubly Linked List
doubly_ll_small = DoublyLinkedList()
doubly_ll_large = DoublyLinkedList()

start = time.time()
for i in range(3):
    doubly_ll_small.insert(i)
end = time.time()
print(f"Time to insert into small Doubly Linked List: {end - start:.8f} seconds")

start = time.time()
for i in range(10000):
    doubly_ll_large.insert(i)
end = time.time()
print(f"Time to insert into large Doubly Linked List: {end - start:.8f} seconds")

start = time.time()
doubly_ll_small.access(1)
end = time.time()
print(f"Time to access small Doubly Linked List: {end - start:.8f} seconds")

start = time.time()
doubly_ll_large.access(9999)
end = time.time()
print(f"Time to access large Doubly Linked List: {end - start:.8f} seconds")

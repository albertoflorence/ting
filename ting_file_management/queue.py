from ting_file_management.abstract_queue import AbstractQueue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(AbstractQueue):
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        node = Node(value)

        if self.top is None:
            self.top = node
        else:
            self.tail.next = node

        self.tail = node
        self.size += 1

        return node.value

    def dequeue(self):
        if self.is_empty():
            raise IndexError(
                "Não é possível remover elementos de uma fila vazia"
            )

        value = self.top.value
        self.top = self.top.next
        self.size -= 1

        if self.size == 0:
            self.top = None

        return value

    def search(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice Inválido ou Inexistente")

        node = self.top
        for i in range(index):
            node = node.next

        return node.value

    def is_empty(self):
        return self.size == 0

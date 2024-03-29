class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.top = Node()
        self.tail = None

    def append(self, value):
        
        if self.tail is None:
            current = self.top
            current.next_node = Node(value)
            self.tail = current.next_node
            return

        current = self.tail
        current.next_node = Node(value)
        self.tail = current.next_node

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
print(lst.__str__())

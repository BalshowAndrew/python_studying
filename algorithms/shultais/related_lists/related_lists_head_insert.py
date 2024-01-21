class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.top = Node()
        self.tail = None
        
    def append(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.top.next_node = new_node
            self.tail = new_node
            return

        self.tail.next_node = new_node
        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.top.next_node = new_node
            self.tail = new_node
            return

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


lst = List()
lst.prepend(0)
lst.prepend(-1)
lst.prepend(-2)
lst.prepend(-3)
# print(lst)
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
print(lst)

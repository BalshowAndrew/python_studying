class Node:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return self.key, self.value


class List:

    def __init__(self):
        # Ограничитель.
        self.top = Node()

    def append(self, key, value):
        """
        Добавление нового узла в конец связанного списка.
        Время работы O(N).
        """
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(key, value)

    def find(self, key):
        """
        Ищет ячейку в связанном списке по значению key и возвращает value.
        Если элемента с искомым key в списке нет, возвращает None.
        """
        current = self.top
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next_node
        return None
            
    def __str__(self):
        """
        Возвращает все элементы связанного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current.value) + end
            current = current.next_node

        return values + "]"


lst = List()

lst.append(0, 'A')
lst.append(1, 'B')
lst.append(2, 'C')
lst.append(3, 'D')
print(lst)
print(lst.find(2))
print(lst.find(4))

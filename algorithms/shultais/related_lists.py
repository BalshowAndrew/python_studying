class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.key, self.value


class List:

    def __init__(self):
        self.head = None # Ссылка на первый элемент списка

    def append(self, key, value):
        """
        Добавление нового узла в конец связанного списка.
        Время работы O(N).
        """
        # Если нет первого элемента, то создаем его и завершаем работу.
        if self.head is None:
            self.head = Node(key, value)
            return
        
        # Перебираем поочереди все элементы, чтобы найти последний
        current = self.head
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(key, value)

    # def find(self, key):
    #     current = self.head
    #     while current.next_node is not None:
    #         if current.key == key:
    #             return current.value
    #         break
            
        

    def __str__(self):
        """
        Возвращает все элементы связанного списка в виде строки.
        """
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current.value) + end
            current = current.next_node

        return values + "]"


# node1 = Node(0, 75)
#
# node2 = Node(1, 12)
# node1.next_node = node2
#
# node3 = Node(2, 28)
# node2.next_node = node3
#
# node4 = Node(3, 6)
# node3.next_node = node4
#
# print(node1.key)
# print(node1.value)
# print(node1.__str__())
# print(node1.next_node.value)


lst = List()

lst.append(0, 75)
lst.append(1, 12)
lst.append(2, 28)
lst.append(3, 6)
print(lst)

current = lst.head
while current is not None:
    # print(str(current.key) + ', ' + str(current.value))
    print(current.key, current.value)
    current = current.next_node


# while current.next_node is not None:
#     print(current.key, current.value)


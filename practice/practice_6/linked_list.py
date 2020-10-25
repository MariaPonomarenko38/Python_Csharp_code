class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes[0])
            self.head = node
            for elem in range(1, len(nodes)):
                node.next = Node(nodes[elem])
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def length(self):
        k = 0
        for node in self:
            k += 1
        return k

    def push_back(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def pop_node(self, pos):
        current_node = self.head
        prev = 0
        if current_node is not None:
            if pos == 1:
                self.head = current_node.next
                return
        k = 0
        while current_node is not None:
            k += 1
            if k == pos:
                break
            prev = current_node
            current_node = current_node.next
        prev.next = current_node.next

    def pop_range_of_nodes(self, pos1, pos2):
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1
        k = 0
        l = pos2 - pos1 + 1
        for node in self:
            k += 1
            if k <= l:
                self.pop_node(pos1)

    def insert_node(self, pos, new_data):
        k = 1
        current_node = self.head
        if k == pos:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        for node in self:
                k += 1
                if k == pos:
                    current_node = node
        new_node = Node(new_data)
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_list(self, pos, ls):
        if self.length() != 0 or pos < self.length():
            for i, elem in enumerate(ls):
                self.insert_node(pos + i, elem)
        else:
            for i in ls:
                self.push_back(i)

    def get_negative_node(self, param):
        current = self.head
        next1 = current.next
        answer = 0
        while next1:
            if current.data < 0:
                answer = current
                if param == "first":
                    return answer
            current = next1
            next1 = current.next
        if current.data < 0:
            answer = current
        return answer.data if answer != 0 else answer

    def negative_k_cycle(self, k):
        for i in range(k):
            k1 = 0
            t = 0
            last_node_data = self.get_negative_node("last")
            if last_node_data == 0:
                return self
            for node in self:
                if node.data < 0 and k1 == 0:
                    t_data = node.data
                    k1 += 1
                elif node.data < 0 and k1 > 0:
                    s_data = node.data
                    node.data = t_data
                    t_data = s_data
            first_node = self.get_negative_node("first")
            if first_node == 0:
                return
            first_node.data = last_node_data
        return self

    def reverse_positive(self):
        list_1 = LinkedList()
        for node1 in self:
            if node1.data >= 0:
                list_1.push_back(node1.data)
        prev = None
        current = list_1.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        list_1.head = prev
        current1 = list_1.head
        for node1 in self:
            if node1.data >= 0:
                node1.data = current1.data
                current1 = current1.next
        return self

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes = list(map(str, nodes))
        return " ".join(nodes)
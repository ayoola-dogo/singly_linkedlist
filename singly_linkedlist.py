class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.root = None
        self.num_of_nodes = 0

    def number_of_nodes(self):
        print(self.num_of_nodes)

    # Insert at the start operation has a O(1) constant running time complexity
    def insert_start(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.num_of_nodes += 1
        else:
            temp_node = self.root
            self.root = new_node
            self.root.next = temp_node
            self.num_of_nodes += 1

    # Insert at the end operation has a O(N) linear running time complexity
    def insert_end(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.num_of_nodes += 1
        else:
            self.insert_node(data, node=self.root)

    def insert_node(self, data, node):
        if node.next is not None:
            self.insert_node(data, node.next)
        else:
            new_node = Node(data)
            node.next = new_node
            self.num_of_nodes += 1

    # The search operation has a O(N) linear running time complexity
    def search(self, data):
        if self.root:
            current_node = self.root
            while current_node is not None and current_node.data != data:
                current_node = current_node.next
            else:
                if current_node is not None and current_node.data == data:
                    print(current_node.data)
                else:
                    print("Node with that data is not present")

    # Removing a node at the start is a O(1) constant running time complexity
    def remove_start(self):
        if self.root:
            temp_node = self.root
            if temp_node.next:
                self.root = temp_node.next
            else:
                self.root = None
            self.num_of_nodes -= 1

    # Removing a node at anywhere else has a O(N) linear running time complexity
    def remove(self, data):
        if self.root:
            current_node = self.root
            if self.root.data == data:
                self.remove_start()
            else:
                self.remove_node(data, None, current_node)

    def remove_node(self, data, previous_node, current_node):
        if current_node is not None and current_node.data != data:
            prev_node = current_node
            curr_node = current_node.next
            self.remove_node(data, prev_node, curr_node)
        elif current_node is not None and current_node.data == data:
            previous_node.next = current_node.next
            self.num_of_nodes -= 1
        else:
            print("Node does not exist")

    # Traverse the singly linked list operation has a O(N) running time complexity
    def traverse(self):
        if self.root is not None:
            self.traverse_node(self.root)

    def traverse_node(self, node):
        print(node.data)
        if node.next:
            self.traverse_node(node.next)


if __name__ == "__main__":
    singlyLinkedList = SinglyLinkedList()
    singlyLinkedList.insert_end(12)
    singlyLinkedList.insert_end(7)
    singlyLinkedList.insert_end(13)
    singlyLinkedList.insert_end(15)
    singlyLinkedList.insert_end(14)
    singlyLinkedList.insert_end(9)
    # singlyLinkedList.insert_end(1)
    # singlyLinkedList.insert_end(9)
    # singlyLinkedList.insert_start(100)

    singlyLinkedList.traverse()
    print("---------------------------------------------------------------------------------------------------------")
    singlyLinkedList.number_of_nodes()
    print("---------------------------------------------------------------------------------------------------------")
    singlyLinkedList.search(1000)
    print("-----------------------------Remove starting node---------------------------------------------------------")
    singlyLinkedList.remove_start()
    singlyLinkedList.traverse()
    print("-----------------------------Remove node anywhere else----------------------------------------------------")
    singlyLinkedList.remove(9)
    singlyLinkedList.traverse()

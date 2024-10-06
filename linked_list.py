# SHAHEER NASIR (021842158) #
# DSA456V1B #
# OCT 6, 2024 # 

# node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list
class Linked_List:

    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def is_empty(self) -> bool:
        return self.head.data is None # if none return true else false
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head # new node has to connect to current head
        self.head = new_node # new head is the new node
        self.length += 1 # add 1 to list

    def append(self, data):
        new_node = Node(data) 
        self.tail.next = new_node
        self.tail = new_node # tail connects to new node
        self.length += 1 # add 1 to list
    
    # insert_self(self, target: Node, data: Any)

    def delete(self, target: data) -> bool: # unfinished
        node = self.head
    
        while node:
            if node.data == data:
                # prev node = node.next 
                node.next = None # this'll delete node 
                
            else:
                # prev node needs to get stored
                node = node.next

    # def delete(self, target: Node)

    def search(self, data: any):
        node = self.head 
        while node:
            if node.data == data:
                return node # return memory of node if data is found
            else:
                node = node.next

    def to_list(self) -> list[any]:
        list = [] # list to store data 
        node = self.head
        while node:
            list.append(node.data) # append data to list
            node = node.next 
        return list

    def size(self):
        return self.length

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    


l = Linked_List(24)
l.append(41)
l.prepend(211)
l.append(42)
l.append(44)



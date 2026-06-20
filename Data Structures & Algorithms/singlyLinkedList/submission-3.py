class Node:
    value: int
    next_node: Node

    def __init__(self, value: int, link_to: Node = None):
        self.value = value
        self.next_node = link_to

    def get_value(self) -> int:
        return self.value
    
    def link_to(self, link_to: Node):
        self.next_node = link_to

    def get_next(self):
        return self.next_node

class LinkedList:
    head: Node
    tail: Node
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index < 0 or self.head == None: return -1
        current = self.head
        for i in range(index):
            if current.get_next() == None: return -1
            current = current.get_next()
        return current.get_value()

    def insertHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None)
            self.tail = self.head
            return
        #if self.head == self.tail:
        #    self.head = Node(val, self.tail)
        #    return
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        new_tail = Node(val, None)
        if self.head == None:
            self.head = new_tail
            self.tail = self.head
            return
        #if self.head == self.tail:
        #    self.tail = new_tail
        #    self.head.link_to(self.tail)
        #    return
        self.tail.link_to(new_tail)
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        if index < 0 or self.head == None: return False

        if index == 0:
            self.head = self.head.get_next()
            if self.head == None: self.tail = None
            return True

        current = self.head
        for i in range(index-1):
            if current.get_next() == None: return False
            current = current.get_next()
        to_remove = current.get_next()
        if to_remove == None: return False
        current.link_to( to_remove.get_next() )
        if current.get_next() == None: self.tail = current
        return True

    def getValues(self) -> List[int]:
        value_list = []
        current = self.head
        while current != None:
            value_list.append(current.get_value())
            current = current.get_next()
        return value_list
        

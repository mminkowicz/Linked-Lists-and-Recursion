
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """
        Creates a new node and inserts it at the front of the list in O(1) time.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Creates a new node and appends it to the end of the list in O(n) time.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Returns the sum of all node data using a recursive helper.
        Recursion is used here to elegantly traverse the list without explicit looping.
        """
        def _sum_helper(node):
            # Base case: empty list or end of list
            if node is None:
                return 0
            # Recursive case: current data + sum of the rest
            return node.data + _sum_helper(node.next)

        return _sum_helper(self.head)

    def recursive_reverse(self):
        """
        Reverses the list in-place using a recursive helper.
        Each recursive call re-points a node's next reference to the previous node.
        """
        def _reverse_helper(prev, current):
            # Base case: reached the end; prev is the new head
            if current is None:
                return prev
            # Recursive case: save next, point current back to prev, advance
            next_node = current.next
            current.next = prev
            return _reverse_helper(current, next_node)

        self.head = _reverse_helper(None, self.head)

    def recursive_search(self, target):
        """
        Returns True if target is found in the list, False otherwise.
        Recursion provides a clean base-case / recursive-case pattern for traversal.
        """
        def _search_helper(node):
            # Base case: end of list without finding the target
            if node is None:
                return False
            # Base case: found the target
            if node.data == target:
                return True
            # Recursive case: search the rest of the list
            return _search_helper(node.next)

        return _search_helper(self.head)

    def display(self):
        """
        Prints the list in the format: val -> val -> val -> None
        """
        parts = []
        current = self.head
        while current:
            parts.append(str(current.data))
            current = current.next
        print(" -> ".join(parts) + " -> None")

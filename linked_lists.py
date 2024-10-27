class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: 'Node' = None


def reverse_linked_list(head: Node) -> Node:
    """
    Reverses a singly linked list.

    :param head: Head of the singly linked list.
    :return: New head of the reversed list.
    """
    prev: Node = None
    current: Node = head
    while current:
        next_node: Node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # new head


def insertion_sort_linked_list(head: Node) -> Node:
    """
    Sorts a singly linked list using the insertion sort algorithm.

    :param head: Head of the singly linked list.
    :return: Head of the sorted list.
    """
    sorted_list: Node = None
    current: Node = head
    while current:
        next_node: Node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node
    return sorted_list


def sorted_insert(sorted_list: Node, new_node: Node) -> Node:
    """
    Inserts a new node into the sorted list.

    :param sorted_list: The sorted list.
    :param new_node: The new node to insert.
    :return: The sorted list with the new node inserted.
    """
    if sorted_list is None or sorted_list.data >= new_node.data:
        new_node.next = sorted_list
        return new_node
    else:
        current: Node = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return sorted_list


def merge_sorted_linked_lists(list1: Node, list2: Node) -> Node:
    """
    Merges two sorted singly linked lists into one sorted list.

    :param list1: The first sorted list.
    :param list2: The second sorted list.
    :return: The merged sorted list.
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data <= list2.data:
        merged_head = list1
        list1 = list1.next
    else:
        merged_head = list2
        list2 = list2.next

    current: Node = merged_head
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return merged_head

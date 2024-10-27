# Testing
from linked_lists import (
    Node, insertion_sort_linked_list,
    reverse_linked_list, merge_sorted_linked_lists,
)


def test_insertion_sort_linked_list():
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)
    sorted_head = insertion_sort_linked_list(head)

    assert sorted_head.data == 1
    assert sorted_head.next.data == 2
    assert sorted_head.next.next.data == 3
    print("Test passed for insertion_sort_linked_list.")


def test_reverse_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    reversed_head = reverse_linked_list(head)

    assert reversed_head.data == 3
    assert reversed_head.next.data == 2
    assert reversed_head.next.next.data == 1
    print("Test passed for reverse_linked_list.")


def test_merge_sorted_linked_lists():
    list1 = Node(1)
    list1.next = Node(3)
    list2 = Node(2)
    list2.next = Node(4)
    merged_head = merge_sorted_linked_lists(list1, list2)

    assert merged_head.data == 1
    assert merged_head.next.data == 2
    assert merged_head.next.next.data == 3
    assert merged_head.next.next.next.data == 4
    print("Test passed for merge_sorted_linked_lists.")


if __name__ == "__main__":
    test_reverse_linked_list()
    test_insertion_sort_linked_list()
    test_merge_sorted_linked_lists()

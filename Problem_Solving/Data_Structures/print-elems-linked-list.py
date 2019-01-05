#!/usr/bin/env python3
# coding: utf-8
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = SinglyLinkedListNode(data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)

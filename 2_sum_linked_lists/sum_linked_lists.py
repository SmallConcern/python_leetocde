class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.root = None

    def append(self, num):
        current_node = self.root
        if not current_node:
            self.root = ListNode(num)
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = ListNode(num)

    @staticmethod
    def add_two_linked_lists(l1, l2):
        output_list = LinkedList()


    @staticmethod
    def linked_list_from_num(num):
        num_str = str(num)
        ll = LinkedList()
        for num in num_str:
            ll.append(int(num))
        return ll

    @staticmethod
    def linked_list_to_str(linked_list):
        output_str = ''
        current_node = linked_list.root
        while current_node:
            output_str += str(current_node.val)
            current_node = current_node.next
        return output_str



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        pass

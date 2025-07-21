# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Hitung panjang linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Hitung rotasi yang efektif
        k = k % length
        if k == 0:
            return head

        # Temukan node sebelum titik rotasi baru
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # sambungkan akhir list ke head lama

        return new_head

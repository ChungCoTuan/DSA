# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Nếu danh sách rỗng hoặc chỉ có 1 phần tử không có con trỏ next
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Thỏ chạy nhanh gấp đôi Rùa
        while fast and fast.next:
            slow = slow.next          # Rùa đi 1 bước
            fast = fast.next.next     # Thỏ đi 2 bước
            
            # Nếu chúng gặp nhau, chứng tỏ có vòng lặp
            if slow == fast:
                return True
                
        # Nếu thoát khỏi vòng lặp, nghĩa là Thỏ đã chạm đích (None) -> Không có vòng
        return False
        
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # lưu node tiếp theo
            curr.next = prev        # đảo chiều
            prev = curr             # tiến prev
            curr = next_node        # tiến curr
        
        return prev
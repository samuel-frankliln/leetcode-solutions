class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Compute the length and get the tail node
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Compute effective rotations needed
        k = k % length
        if k == 0:
            return head  # Corrected to return head instead of 0
        
        # Step 3: Find the new tail node (at position length - k - 1)
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        
        # Step 4: Re-link the nodes to rotate the list
        new_head = curr.next
        curr.next = None
        tail.next = head
        
        return new_head

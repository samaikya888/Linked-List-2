'''
Approach: Divide the problem into 3 parts: Find the mid of linked list, Reverse the second half of the linkedlist and merge by adding each node of second reversed list to first list alternatively

Time Complexity: O(N)
Space Complexity: O(1)

Passes all testcases in leetcode

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None: return
        
        #Find middle
        slow = head
        fast = head
        
        while(fast and fast.next):
            prev1 = slow
            slow = slow.next
            fast = fast.next.next
            
        #print(head)
        #print(slow)
        
        
        #Reverse from slow
        prev = None 
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node       

        #Merging
        p1 = head
        p2 = prev
        while p2.next:
            t1 = p1.next
            p1.next = p2
            p1 = t1
            
            t2 = p2.next
            p2.next = p1
            p2 = t2
            

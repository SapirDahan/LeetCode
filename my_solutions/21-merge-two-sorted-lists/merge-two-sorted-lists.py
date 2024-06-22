# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:   

        # Create ne list    
        newList = ListNode()
        current = newList

        while list1 is not None and list2 is not None:
            
            # If list1 is empty
            if list1 is None:
                current.next = list2
                break

            # If list2 is empty
            if list2 is None:
                current.next = list1
                break

            # Append the new list with the correctnode
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Append the remaining elements
        if list1 is not None:
            current.next = list1
        if list2 is not None:
            current.next = list2

        return newList.next
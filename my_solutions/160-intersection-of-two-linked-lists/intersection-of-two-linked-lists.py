# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        visited = set()
        currentA, currentB = headA, headB
        while currentA or currentB:
            if currentA:
                if currentA in visited:
                    return currentA
                visited.add(currentA)
                currentA = currentA.next
            if currentB:
                if currentB in visited:
                    return currentB
                visited.add(currentB)
                currentB = currentB.next
        return None
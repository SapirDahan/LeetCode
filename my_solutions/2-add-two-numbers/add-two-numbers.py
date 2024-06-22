# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Calculate the first number
        num1 = 0
        factor = 1  # Initialize factor to 1 for the first number
        current = l1

        while current is not None:
            num1 += current.val * factor
            factor *= 10
            current = current.next

        # Calculate the second number
        num2 = 0
        factor = 1  # Initialize factor to 1 for the second number
        current = l2

        while current is not None:
            num2 += current.val * factor
            factor *= 10
            current = current.next

        # Sum the two numbers
        totalNumber = num1 + num2

        # Create the resulting list
        dummy = ListNode()  # Dummy node to simplify list creation
        current = dummy

        # If the total sum is zero, return a single node with value 0
        if totalNumber == 0:
            return ListNode(0)
        
        # Convert the totalNumber back to a linked list
        while totalNumber > 0:
            current.next = ListNode(totalNumber % 10)  # Create new node with the last digit of totalNumber
            totalNumber //= 10  # Remove the last digit from totalNumber
            current = current.next  # Move to the next node

        return dummy.next  # Return the head of the resulting list, skipping the dummy node
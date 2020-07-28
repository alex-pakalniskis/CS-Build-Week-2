# https://leetcode.com/problems/add-two-numbers/

"""2. Add Two Numbers (Medium)

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize ListNode to contain results
        result = ListNode(0)
        # Set a pointer for later use
        result_tail = result
        # Create variable to store carried values during addition
        carry = 0
                
        while l1 or l2 or carry:
            # Loop thru ListNodes until end is reached            
            value_1  = (l1.val if l1 else 0)
            value_2  = (l2.val if l2 else 0)
            # Calculate sum of and update carry value with divmod operation
            # Returns tuple of quotient and remainder (carry = quotient, out = remainder)
            carry, out = divmod(value_1 + value_2 + carry, 10)    
            # Create new ListNode with out value
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            # Move along ListNode
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next
        
        
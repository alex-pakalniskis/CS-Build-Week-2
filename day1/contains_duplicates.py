# https://leetcode.com/problems/contains-duplicate/

"""
217. Contains Duplicate (Easy)
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Since sets contain no duplicates, use a set representation of nums to quickly
        # check if there are duplicates, comparing the number of items in set(nums)
        # with the number of items if nums
        if len(set(nums)) < len(nums):
            # Return True if number of entries in set(nums) is 
            # less than the number of entries in nums
            return True
        else:
            # Otherwise, if number of entries is equal in both 
            # return False
            return False
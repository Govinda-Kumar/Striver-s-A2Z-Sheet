'''
Check if the Array is Sorted II
-------------------------------------------------
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


Example 1

Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Example 2

Input : nums = [1, 2, 1, 4, 5]

Output : false

Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

Constraints

1 <= n <= 100
1 <= nums[i] <= 100

'''
class Solution:
    # Approach - 1
    # def isSorted(self, nums):
    #     for i in range(1, len(nums)):
    #         if nums[i] < nums[i - 1]:
    #             print(False)
    #             return
    #     print(True)
    
    
    # Approach - 2
    def isSorted(self, nums):
        print(all(a <= b for a, b in zip(nums, nums[1:])))
    

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.isSorted([8, 8, 7, 6, 5])
    sol.isSorted([10, 10, 10, 10, 10])
    sol.isSorted([-5, -10, -3])
    sol.isSorted([1, 2, 3, 4, 5])
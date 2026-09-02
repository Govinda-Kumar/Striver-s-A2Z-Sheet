'''
Bubble Sort
-----------------------------------------------------------------
Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.



A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.


Example 1

Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]

Explanation: 1 <= 3 <= 4 <= 5 <= 7.

Thus the array is sorted in non-decreasing order.

Example 2

Input: nums = [5, 4, 4, 1, 1]

Output: [1, 1, 4, 4, 5]

Explanation: 1 <= 1 <= 4 <= 4 <= 5.

Thus the array is sorted in non-decreasing order.

Constraints

1 <= nums.length <= 1000
-10^4 <= nums[i] <= 10^4
nums[i] may contain duplicate values.
'''

class Solution:
    
    # Approach - 1
    # def bubbleSort(self, nums):
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(1, n):
    #             if nums[j] < nums[j-1]:
    #                 nums[j], nums[j-1] = nums[j-1], nums[j]
    #     return nums
    
    # Approach - 2
    # def bubbleSort(self, nums):
    #     n = len(nums)
    #     for i in range(n - 1, -1, -1):
    #         for j in range(i):
    #             if nums[j] > nums[j+1]:
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]
    #     return nums
    
    # Approach - 3
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(1, n - i):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums    


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.bubbleSort([7, 4, 1, 5, 3]))
    print(sol.bubbleSort([5, 4, 4, 1, 1]))
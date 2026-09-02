'''
Insertion Sort
-----------------------------------------------------------------
Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.



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
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.insertionSort([7, 4, 1, 5, 3]))
    print(sol.insertionSort([5, 4, 4, 1, 1]))
'''
Move Zeros to End
-------------------------------------------------
Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.



This must be done in place, without making a copy of the array.


Example 1

Input: nums = [0, 1, 4, 0, 5, 2]

Output: [1, 4, 5, 2, 0, 0]

Explanation:

Both the zeroes are moved to the end and the order of the other elements stay the same

Example 2

Input: nums = [0, 0, 0, 1, 3, -2]

Output: [1, 3, -2, 0, 0, 0]

Explanation:

All 3 zeroes are moved to the end and the order of the other elements stay the same

Constraints

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''
class Solution:
    # Approach - 1
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        unique = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[unique] = nums[i]
                unique += 1
        return unique

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([0, 0, 3, 3, 5, 6]))
    print(sol.removeDuplicates([-2, -2, 2, 4, 4, 4, 4, 5, 5]))
    print(sol.removeDuplicates([1, 2, 3, 4, 5]))
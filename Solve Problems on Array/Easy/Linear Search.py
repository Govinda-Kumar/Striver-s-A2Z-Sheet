'''
Linear Search
-------------------------------------------------
Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1


Example 1

Input: nums = [2, 3, 4, 5, 3], target = 3

Output: 1

Explanation:

The first occurence of 3 in nums is at index 1

Example 2

Input: nums = [2, -4, 4, 0, 10], target = 6

Output: -1

Explanation:

The value 6 does not occur in the array, hence output is -1

Constraints

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
-10^4 <= target <= 10^4
'''
class Solution:
    # Approach - 1
    # def linearSearch(self, nums, target):
    #     if target not in nums:
    #         return -1
    #     return nums.index(target)
    
    # Approach - 2
    def linearSearch(self, nums, target):
        for idx, val in enumerate(nums):
            if val == target:
                return idx
        return -1


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.linearSearch([1, 2, 3, 4, 8, 3, 0, 0, 6], 8))
    print(sol.linearSearch([0, 2, 0, 0, 4, 0], 0))
    print(sol.linearSearch([1, 2, 3, 0, 0, 6], 3))
    print(sol.linearSearch([2, -4, 4, 0, 10], 6))
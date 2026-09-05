'''
Two Sum
-------------------------------------------------
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.



Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in any order.


Example 1

Input: nums = [1, 6, 2, 10, 3], target = 7

Output: [0, 1]

Explanation:

nums[0] + nums[1] = 1 + 6 = 7

Example 2

Input: nums = [1, 3, 5, -7, 6, -3], target = 0

Output: [1, 5]

Explanation:

nums[1] + nums[5] = 3 + (-3) = 0

Constraints

2 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
-10^5 <= target <= 10^5
Only one valid answer exists.
'''
class Solution:
    # Approach - 1
    # def twoSum(self, nums, target):
    #     compliment = [target - i for i in nums]
    #     for i in range(len(nums)):
    #         if compliment[i] + nums[i] == target and compliment[i] in nums:
    #             return ([i, nums.index(compliment[i])])
    #     return -1
    
    
    # Approach - 2
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i
        return -1
    

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1, 6, 2, 10, 3], 7))
    print(sol.twoSum([1, 3, 5, -7, 6, -3], 0))
    print(sol.twoSum([-6, 7, 1, -7, 6, 2], 3))
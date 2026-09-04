'''
Find missing number
-------------------------------------------------
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.


Example 1

Input: nums = [0, 2, 3, 1, 4]

Output: 5

Explanation:

nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Example 2

Input: nums = [0, 1, 2, 4, 5, 6]

Output: 3

Explanation:

nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]

Constraints

n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
'''
class Solution:
    # Approach - 1
    # def missingNumber(self, nums):
    #     n = len(nums)
    #     numbers = [i for i in range(n + 1)]
    #     for i in numbers:
    #         if i not in nums:
    #             return i
    #     return 0
    
    
    # Approach - 2
    # def missingNumber(self, nums):
    #     n = len(nums)
    #     i = 0
    #     while i < n:
    #         if i not in nums:
    #             return i
    #         i += 1
    #     return n
    
    # Approach - 3
    # def missingNumber(self, nums):
    #     n = len(nums)
    #     return ((n * (n + 1)) // 2) - sum(nums)
    
    # Approach - 4
    def missingNumber(self, nums):
        n = len(nums)
        for i, num in enumerate(nums):
            n ^= i ^ num
        return n

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([1, 3, 6, 4, 2, 5]))
    print(sol.missingNumber([0, 2, 3, 1, 4]))
    print(sol.missingNumber([0, 1, 2, 4, 5, 6]))
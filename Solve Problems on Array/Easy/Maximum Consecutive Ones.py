'''
Maximum Consecutive Ones
-------------------------------------------------
Given a binary array nums, return the maximum number of consecutive 1s in the array.



A binary array is an array that contains only 0s and 1s.


Example 1

Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

Output: 3

Explanation:

The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Example 2

Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]

Output: 0

Explanation:

No 1s are present in nums, thus we return 0

Constraints

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

'''
class Solution:
    # Approach - 1
    # def findMaxConsecutiveOnes(self, nums):
    #     n = len(nums)
    #     cons = 0
    #     t = 0
    #     for i in range(n):
    #         if nums[i] == 1:
    #             t += 1
    #         else:
    #             t = 0
    #         cons = max(cons, t)
    #     return cons
    
    
    # Approach - 2
    # def findMaxConsecutiveOnes(self, nums):
    #     cons = 0
    #     t = 0
    #     for i in nums:
    #         if i == 1:
    #             t += 1
    #         else:
    #             if t > cons:
    #                 cons = t
    #             t = 0
    #     return t if t > cons else cons

    # Approach - 3
    def findMaxConsecutiveOnes(self, nums):
        return max(len(streak) for streak in "".join(map(str, nums)).split("0"))

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1, 1, 0, 0, 1, 1, 1, 1, 0]))
    print(sol.findMaxConsecutiveOnes([0, 0, 0, 0, 0, 0, 0, 0]))
    print(sol.findMaxConsecutiveOnes([1, 0, 1, 1, 1, 0, 1, 1, 1]))
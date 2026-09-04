'''
Single Number - I
-------------------------------------------------
Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.


Example 1

Input : nums = [1, 2, 2, 4, 3, 1, 4]

Output : 3

Explanation : The integer 3 has appeared only once.

Example 2

Input : nums = [5]

Output : 5

Explanation : The integer 5 has appeared only once.

Constraints

1 <= n <= 10^5
-3*10^5 <= nums[i] <= 3*10^5

'''
class Solution:
    # Approach - 1
    # def singleNumber(self, nums):
    #     n = len(nums)
    #     temp = []
    #     for i in range(n):
    #         if nums[i] not in temp:
    #             temp.append(nums[i])
    #         else:
    #             temp.remove(nums[i])
    #     return temp[0]
    
    
    # Approach - 2
    # def singleNumber(self, nums):
    #     n = len(nums)
    #     for i in range(n):
    #         if -nums[i] not in nums:
    #             nums[i] = -nums[i]
    #     return -sum(nums)

    # Approach - 3
    # def singleNumber(self, nums):
    #     return 2 * sum(set(nums)) - sum(nums)
    
    # Approach - 4
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([1, 2, 2, 4, 3, 1, 4]))
    print(sol.singleNumber([5]))
    print(sol.singleNumber([1, 3, 10, 3, 5, 1, 5]))
    # print(sol.singleNumber([5, 5]))
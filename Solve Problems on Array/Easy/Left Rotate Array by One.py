'''
Left Rotate Array by One
-------------------------------------------------
Given an integer array nums, rotate the array to the left by one.



Note: There is no need to return anything, just modify the given array.


Example 1

Input: nums = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation:

Initially, nums = [1, 2, 3, 4, 5]

Rotating once to left -> nums = [2, 3, 4, 5, 1]

Example 2

Input: nums = [-1, 0, 3, 6]

Output: [0, 3, 6, -1]

Explanation:

Initially, nums = [-1, 0, 3, 6]

Rotating once to left -> nums = [0, 3, 6, -1]

Constraints

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''
class Solution:
    # Approach - 1
    # def rotateArrayByOne(self, nums: list[int]):
    #     n = len(nums)
    #     for i in range(1, n):
    #         nums[i], nums[i - 1] = nums[i - 1], nums[i]
    #     return nums

    # Approach - 2
    def rotateArrayByOne(self, nums: list[int]):
        first = nums[0]
        nums[:-1] = nums[1:]
        nums[-1] = first
        return nums

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateArrayByOne([0, 0, 3, 3, 5, 6]))
    print(sol.rotateArrayByOne([-2, -2, 2, 4, 4, 4, 4, 5, 5]))
    print(sol.rotateArrayByOne([1, 2, 3, 4, 5]))
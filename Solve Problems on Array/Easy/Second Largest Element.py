'''
Second Largest Element
-------------------------------------------------
Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


Example 1

Input: nums = [8, 8, 7, 6, 5]

Output: 7

Explanation:

The largest value in nums is 8, the second largest is 7

Example 2

Input: nums = [10, 10, 10, 10, 10]

Output: -1

Explanation:

The only value in nums is 10, so there is no second largest value, thus -1 is returned

Constraints

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
nums may contain duplicate elements.
'''
class Solution:
    # Approach - 1
    def secondLargestElement(self, nums):
        largest = max(nums)
        c = nums.count(largest)
        for i in range(c):
            nums.remove(largest)
        secondLargest = max(nums) if len(nums) else -1
        print(secondLargest)
    
    
    # Approach - 2
    # def secondLargestElement(self, nums):
    #     maximum = float('-inf')
    #     secondLargest = float('-inf')
    #     for i in nums:
    #         if maximum < i:
    #             secondLargest = maximum
    #             maximum = i
    #         if i > secondLargest and maximum != i:
    #             secondLargest = i
    #     print(secondLargest if secondLargest != float('-inf') else -1)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.secondLargestElement([8, 8, 7, 6, 5])
    sol.secondLargestElement([10, 10, 10, 10, 10])
    sol.secondLargestElement([-5, -10, -3])
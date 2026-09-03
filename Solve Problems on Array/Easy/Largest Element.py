'''
Largest Element
-------------------------------------------------
Given an array of integers nums, return the value of the largest element in the array


Example 1

Input: nums = [3, 3, 6, 1]

Output: 6

Explanation: The largest element in array is 6

Example 2

Input: nums = [3, 3, 0, 99, -40]

Output: 99

Explanation: The largest element in array is 99

Constraints

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
nums may contain duplicate elements.
'''
class Solution:
    # Approach - 1
    # def largestElement(self, nums):
    #     print(max(nums))
    
    
    # Approach - 2
    def largestElement(self, nums):
        maximum = nums[0]
        for i in nums:
            if maximum < i:
                maximum = i
        print(maximum)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.largestElement([3, 3, 6, 1])
    sol.largestElement([3, 3, 0, 99, -40])
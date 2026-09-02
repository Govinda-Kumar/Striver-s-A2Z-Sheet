'''
Highest Occurring Element in an Array
-------------------------------------------------
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.



Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!


Example 1

Input: nums = [1, 2, 2, 3, 3, 3]

Output: 3

Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Example 2

Input: nums = [4, 4, 5, 5, 6]

Output: 4

Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

Constraints

1 <= n <= 10^5
1 <= nums[i] <= 10^4
'''

class Solution:

    # Approach - 1
    # def mostFrequentElement(self, nums):
    #     frequencies = {}
    #     for i in nums:
    #         if i in frequencies:
    #             frequencies[i] += 1
    #         else:
    #             frequencies[i] = 1
    #     maximum_key = nums[0]
    #     maximum_val = frequencies[nums[0]]
    #     for key, val in frequencies.items():
    #         if key != maximum_key and val > maximum_val:
    #             maximum_key = key
    #             maximum_val = val
    #     return maximum_key
            
    # Approach - 2
    # def mostFrequentElement(self, nums):
    #     frequencies = {}
    #     maximum_key = nums[0]
    #     maximum_val = 1
    #     for i in nums:
    #         if i in frequencies:
    #             frequencies[i] += 1
    #         else:
    #             frequencies[i] = 1

    #         if maximum_val < frequencies[i]:
    #             maximum_val = frequencies[i]
    #             maximum_key = i
    #     return maximum_key
    
    # Approach - 3
    def mostFrequentElement(self, nums):
        frequencies = {}
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1
        return max(frequencies, key=frequencies.get)

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.mostFrequentElement([1, 2, 2, 3, 3, 3]))
    print(sol.mostFrequentElement([4, 4, 5, 5, 6]))
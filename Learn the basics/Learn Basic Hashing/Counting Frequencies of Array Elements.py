'''
Counting Frequencies of Array Elements
-------------------------------------------------
Given an array nums of size n which may contain duplicate elements.



Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.



You may return the result in any order, but each element must appear exactly once in the output.


Example 1

Input: nums = [1, 2, 2, 1, 3]

Output: [[1, 2], [2, 2], [3, 1]]

Explanation:

- 1 appears 2 times

- 2 appears 2 times

- 3 appears 1 time

Order of output can vary.

Example 2

Input: nums = [5, 5, 5, 5]

Output: [[5, 4]]

Explanation:

- 5 appears 4 times.

Constraints

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

class Solution:

    # Approach - 1
    # def countFrequencies(self, nums):
    #     frequencies = {}
    #     for i in nums:
    #         if i in frequencies:
    #             frequencies[i] += 1
    #         else:
    #             frequencies[i] = 1
    #     return [[key, val] for key, val in frequencies.items()]
            
    # Approach - 2
    def countFrequencies(self, nums):
        frequencies = {}
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1
        return [[key, val] for key, val in frequencies.items()]

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.countFrequencies([1, 2, 2, 1, 3]))
    print(sol.countFrequencies([5, 5, 5, 5]))
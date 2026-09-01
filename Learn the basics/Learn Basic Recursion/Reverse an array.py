'''
Reverse an array
-------------------------------------------------
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.


Example 1

Input: n=5, arr = [1,2,3,4,5]



Output: [5,4,3,2,1]



Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Example 2

Input: n=6, arr = [1,2,1,1,5,1]



Output: [1,5,1,1,2,1]



Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

Constraints

1 <= n <= 10^4

1 <= arr[i] <= 10^5
'''

class Solution:
    
    # Approach - 1
    # def reverse(self, arr: list, n: int):
    #     if n <= 1:
    #         return 
    #     arr[0], arr[n-1] = arr[n-1], arr[0]
    #     sublist = arr[1: n - 1]
    #     self.reverse(sublist, n - 2)
    #     arr[1: n - 1] = sublist
    #     # print(arr)

    # Approach - 2
    def reverse(self, arr: list, n: int):
        def helper(left: int, right: int):
            if left >= right:
                return
            arr[left], arr[right] = arr[right], arr[left]
            helper(left + 1, right - 1)
        helper(0, n - 1)
        # print(arr)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.reverse([1,2,3,4,5,6], 6)
    sol.reverse([2,5,1], 3)
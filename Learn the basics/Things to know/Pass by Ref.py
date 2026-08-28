'''
Pass by Ref
-----------------------------------------------------------------
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

1 <= n <= 104
1 <= arr[i] <= 105
'''

class Solution:
    def reverse(self, arr: list) -> None:
        n = len(arr)
        for i in range(0, n//2):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
        


# code runner
if __name__ == "__main__":
    sol = Solution()
    test_arr = [1,2,1,1,5,1]
    print(f"Original: {test_arr}")
    sol.reverse(test_arr)
    print(f"Reversed: {test_arr}")
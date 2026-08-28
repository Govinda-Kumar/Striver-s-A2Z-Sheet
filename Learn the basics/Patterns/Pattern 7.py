'''
Pattern 7
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    *
   ***
  *****
 *******
*********


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

   *
  ***
 *****
*******


Example 2

Input: n = 2

Output:
 *
***


Constraints

1 <= n <= 100
'''

class Solution:
    # def pattern7(self, n):
    #     for i in range(1, n+1):
    #         for j in range(n, 0, -1):
    #             if i <= j:
    #                 print(" ", end="")
    #             else:
    #                 print("*", end="")
    #         print("*" * i)

    def pattern7(self, n):
        for i in range(1, n+1):
            spaces = " " * (n - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern7(4)
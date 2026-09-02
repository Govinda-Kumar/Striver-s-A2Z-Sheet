'''
Pattern 20
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        * 


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
*      *
**    **
***  ***
********
***  ***
**    **
*      * 


Example 2

Input: n = 2

Output:

*  *
****
*  *

Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern20(self, n):
    #     for i in range(1,n+1):
    #         for j in range(i):
    #             print("*", end="")
    #         for k in range(n-i-1, -1, -1):
    #             print(" ", end="")
    #         for m in range(n-i-1, -1, -1):
    #             print(" ", end="")
    #         for l in range(i):
    #             print("*", end="")
    #         print("")
    #     for i in range(n-1, 0, -1):
    #         for j in range(i):
    #             print("*", end="")
    #         for k in range(n-i-1, -1, -1):
    #             print(" ", end="")
    #         for m in range(n-i-1, -1, -1):
    #             print(" ", end="")
    #         for l in range(i):
    #             print("*", end="")
    #         print("")

    # Approach - 2

    # def pattern20(self, n):
    #     rows = []
    #     spaces = [(" " * 2 * i) for i in range(n)]
    #     stars = ["*" * i for i in range(1, n+1)]
    #     for j in range(n-1):
    #         rows.append(stars[j] + spaces[::-1][j] + stars[j])
    #     for i in range(n):
    #         rows.append(stars[::-1][i] + spaces[i] + stars[::-1][i])
    #     print("\n".join(rows))
    
    # Approach - 3
    
    def pattern20(self, n):
        print("\n".join((top := ["*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1) for i in range(n)]) + top[n - 2::-1]))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern20(4)
    # sol.pattern20(2)
    # sol.pattern20(5)
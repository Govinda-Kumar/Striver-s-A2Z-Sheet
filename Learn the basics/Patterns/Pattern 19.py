'''
Pattern 19
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

********
***  ***
**    **
*      *
*      *
**    **
***  ***
********



Example 2

Input: n = 2

Output:

****
*  *
*  *
****

Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern19(self, n):
    #     for i in range(n, 0, -1):
    #         for j in range(i):
    #             print("*", end="")
    #         for k in range(n-i-1, -1, -1):
    #             print(" ", end="")
    #         for m in range(n-i-1, -1, -1):
    #             print(" ", end="")
    #         for l in range(i):
    #             print("*", end="")
    #         print("")
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


    # Approach - 2

    # def pattern19(self, n):
    #     rows = []
    #     spaces = [(" " * 2 * i) for i in range(n)]
    #     stars = ["*" * i for i in range(1, n+1)]
    #     for i in range(n):
    #         rows.append(stars[::-1][i] + spaces[i] + stars[::-1][i])
    #     for j in range(n):
    #         rows.append(stars[j] + spaces[::-1][j] + stars[j])
    #     print("\n".join(rows))
    
    # Approach - 3
    
    def pattern19(self, n):
        print("\n".join((top := ["*" * (n - i) + " " * (2 * i) + "*" * (n - i) for i in range(n)]) + top[::-1]))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern19(4)
    # sol.pattern19(2)
    # sol.pattern19(5)
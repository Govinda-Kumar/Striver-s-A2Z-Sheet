'''
Pattern 21
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
*   *
*   *
*   *
***** 


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

****
*  *
*  *
**** 


Example 2

Input: n = 2

Output:

**
**

Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern21(self, n):
    #     for i in range(1,n+1):
    #         for j in range(1, n+1):
    #             if i in (1, n) or j in (1, n):
    #                 print("*", end="")
    #             else:
    #                 print(" ", end="")
    #         print("")

    # Approach - 2

    # def pattern21(self, n):
    #     if n <= 0:
    #         return 
    #     if n == 1:
    #         print("*")
    #         return 
    #     solid_row = "*" * n
    #     hollow = "*" + " " * (n - 2) + "*"
    #     rows = [solid_row] + [hollow] * (n - 2) + [solid_row]
    #     print("\n".join(rows))
        
        
    # Approach - 3
    
    def pattern21(self, n):
        print("*" if n == 1 else "\n".join(([s := "*" * n] + ["*" + " " * (n - 2) + "*"] * (n - 2) + [s])))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern21(4)
    # sol.pattern21(2)
    # sol.pattern21(5)
'''
Pattern 9
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
    * 
   ***
  *****
 *******
 *******
  *****
   ***
    *


Example 2

Input: n = 2

Output:
    * 
   ***
   ***
    *


Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern9(self, n):
    #     for i in range(1, n+1):
    #         for j in range(n, 0, -1):
    #             if i <= j:
    #                 print(" ", end="")
    #             else:
    #                 print("*", end="")
    #         print("*" * i)
    #     for i in range(n, 0, -1):
    #         for j in range(n, 0, -1):
    #             if i <= j:
    #                 print(" ", end="")
    #             else:
    #                 print("*", end="")
    #         print("*" * i)

    
    # Approach - 2

    # def pattern9(self, n):
    #     for i in range(1, n+1):
    #         spaces = " " * (n - i)
    #         stars = "*" * (2 * i - 1)
    #         print(spaces + stars)
    #     for i in range(0, n):
    #         spaces = " " * i
    #         stars = "*" * (2 * (n - i) - 1 )
    #         print(spaces + stars)

    
    # Approach - 3

    def pattern9(self, n):
        for i in range(1, n + 1):
            print(f"{' ' * (n - i)}{"*" * (2 * i - 1)}")
        for i in range(n, 0, -1):
            print(f"{' ' * (n - i)}{"*" * (2 * i - 1)}")

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern9(4)
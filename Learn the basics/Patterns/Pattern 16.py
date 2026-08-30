'''
Pattern 16
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

BB

CCC

DDDD

EEEEE



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

A

BB

CCC

DDDD


Example 2

Input: n = 2

Output:

A

BB


Constraints

1 <= n <= 26
'''

class Solution:

    # Approach - 1

    # def pattern16(self, n):
    #     for i in range(65, 65+n):
    #         for j in range(65, i+1):
    #             print(chr(i), end="")
    #         print()


    # Approach - 2

    # def pattern16(self, n):
    #     for i in range(0, n):
    #         print(chr(65 + i) * (i + 1))
    
    # Approach - 3

    def pattern16(self, n):
        print("\n".join(chr(65 + i) * (i + 1) for i in range(n)))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern16(4)
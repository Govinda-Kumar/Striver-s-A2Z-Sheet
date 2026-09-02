'''
Pattern 18
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



E 

D E 

C D E 

B C D E 

A B C D E 



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
D

C D

B C D

A B C D


Example 2

Input: n = 2

Output:
B

A B

Constraints

1 <= n <= 26
'''

class Solution:

    # Approach - 1

    # def pattern18(self, n):
    #     for i in range(65+n-1, 65-1, -1):
    #         for j in range(i, 65+n):
    #             print(chr(j), end = "")
    #         print()


    # Approach - 2

    def pattern18(self, n):
        alpha = "".join(chr(j) for j in range(65, 65 + n))
        for i in range(n - 1, -1, -1):
            print(alpha[i:])


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern18(4)
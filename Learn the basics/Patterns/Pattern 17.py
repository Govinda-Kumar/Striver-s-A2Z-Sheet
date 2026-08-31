'''
Pattern 17
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

    A
   ABA
  ABCBA
 ABCDCBA

Example 2

Input: n = 2

Output:

    A
   ABA

Constraints

1 <= n <= 26
'''

class Solution:

    # Approach - 1

    # def pattern17(self, n):
    #     for i in range(65, 65+n):
    #         print(" " * (65 + n - i), end = "")
    #         for j in range(65, i+1):
    #             print(chr(j), end = "")
    #         for k in range(n+65-1, 65-1, -1):
    #             if k<i:
    #                 print(chr(k), end = "")
    #         print()


    # Approach - 2

    def pattern17(self, n):
        rows = []
        for i in range(1, n+1):
            spaces = " "*(n - i)
            left = "".join(chr(65 + j) for j in range(i))
            final = left + left[-2::-1]
            rows.append(spaces + final)
        print("\n".join(rows))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern17(4)
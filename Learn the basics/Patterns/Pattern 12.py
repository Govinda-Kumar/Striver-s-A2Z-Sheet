'''
Pattern 12
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1        1
12      21
123    321
1234  4321
1234554321


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
1      1
12    21
123  321
12344321


Example 2

Input: n = 2

Output:
1  1
1221


Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern12(self, n):
    #     for i in range(1, n + 1):
    #         for j in range(1, n + 1):
    #             if j <= i:
    #                 print(j, end="")
    #             else:
    #                 print(" ", end="")
    #         for k in range(n, 0, -1):
    #             if k <= i:
    #                 print(k, end="")
    #             else:
    #                 print(" ", end="")
    #         print()

    
    # Approach - 2

    def pattern12(self, n):
        for i in range(1, n + 1):
            nums = "".join(str(j) for j in range(1, i + 1))
            spaces = " " * (2 * (n-i))
            print(nums + spaces + nums[::-1])

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern12(4)
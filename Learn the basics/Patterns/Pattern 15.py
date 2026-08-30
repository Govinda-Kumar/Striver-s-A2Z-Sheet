'''
Pattern 15
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



ABCDE

ABCD

ABC

AB

A



Print the pattern in the function given to you.

Example 1

Input: n = 4

Output:

ABCD

ABC

AB

A


Example 2

Input: n = 2

Output:

AB

A


Constraints

1 <= n <= 26
'''

class Solution:

    # Approach - 1

    def pattern15(self, n):
        for i in range(n+65-1, 65-1, -1):
            for j in range(65, i+1):
                print(chr(j), end="")
            print()

    
    # Approach - 2

    def pattern15(self, n):
        full_row = "".join(chr(65 + i) for i in range(n))
        rows = [full_row[:i] for i in range(n, 0, -1)]
        print("\n".join(rows))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern15(4)
'''
Pattern 4
----------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


1

22

333

4444

55555



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
1

22

333

4444


Example 2

Input: n = 2

Output:
1

22


Constraints

1 <= n <= 100
'''

class Solution:
    def pattern4(self, n):
        for i in range(1, n+1):
            print(str(i) * i)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern4(5)
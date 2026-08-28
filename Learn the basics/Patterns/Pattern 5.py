'''
Pattern 5
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****

****

***

**

*



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

****

***

**

*


Example 2

Input: n = 2

Output:

**

*


Constraints

1 <= n <= 100

'''

class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            print("*" * i)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern5(5)
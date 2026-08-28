'''
Pattern 6
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


12345

1234

123

12

1



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

1234

123

12

1


Example 2

Input: n = 2

Output:

12

1


Constraints

1 <= n <= 100
'''

class Solution:
    # def pattern6(self, n):
    #     for i in range(n, 0, -1):
    #         for j in range(1, i+1):
    #             print(j, end="")
    #         print()

    def pattern6(self, n):
        base_string = "".join(str(x) for x in range(1, n+1))
        for i in range(n, 0, -1):
            print(base_string[:i])


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern6(5)
'''
Pattern 3
--------------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


1

12

123

1234

12345



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
1

12

123

1234


Example 2

Input: n = 2

Output:
1

12

Constraints

1 <= n <= 100
'''

class Solution:
        
    # Approach - 1

    # def pattern3(self, n):
    #     for i in range(1, n+1):
    #         for j in range(1, i+1):
    #             print(j, end="")
    #         print()

    
    # Approach - 2

    def pattern3(self, n):
        base_string = "".join(str(x) for x in range(1, n+1))
        for i in range(1, n+1):
            print(base_string[:i])

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern3(5)
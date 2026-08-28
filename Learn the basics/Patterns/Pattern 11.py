'''
Pattern 11
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:
1 

0 1 

1 0 1 

0 1 0 1 


Example 2

Input: n = 2

Output:
1 

0 1 


Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern11(self, n):
    #     for i in range(1, n+1):
    #         for j in range(0, i):
    #             print((i+j)%2, end="")
    #         print()

    
    # Approach - 2

    def pattern11(self, n):
        base_string = "".join(str(x%2) for x in range(1, n+1))
        for i in range(n-1, -1, -1):
            print(base_string[i:])

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern11(5)
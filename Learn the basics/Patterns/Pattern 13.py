'''
Pattern 13
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:



Example 2

Input: n = 2

Output:



Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern13(self, n):
    #     c = 1
    #     for i in range(1, n + 1):
    #         for j in range(1, i + 1):
    #             print(c, end=" ")
    #             c += 1
    #         print()

    
    # Approach - 2

    def pattern13(self, n):
        c = 1
        rows = []
        for i in range(1, n + 1):
            rows.append(" ".join(map(str, range(c, c + i))))
            c += i
        print("\n".join(rows))

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern13(4)
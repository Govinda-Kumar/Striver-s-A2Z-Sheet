'''
Pattern 14
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

AB

ABC

ABCD

ABCDE



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

A

AB

ABC

ABCD


Example 2

Input: n = 2

Output:

A

AB


Constraints

1 <= n <= 26
'''

class Solution:

    # Approach - 1

    # def pattern14(self, n):
    #     for i in range(65, n+65):
    #         for j in range(65, i+1):
    #             print(chr(j), end="")
    #         print()

    
    # Approach - 2

    # def pattern14(self, n):
    #     rows = []
    #     for i in range(1, n + 1):
    #         rows.append("".join(chr(j) for j in range(65, 65 + i)))
    #     print("\n".join(rows))


    # Approach - 3

    def pattern14(self, n):
        rows = []
        current_row = ""
        for i in range(n):
            current_row += chr(65 + i)
            rows.append(current_row)
        print("\n".join(rows))

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern14(4)
'''
Pattern 10
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*

**

***

****

*****

****

***

**

*



Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

*

**

***

****

***

**

*

Example 2

Input: n = 2

Output:
*

**

*


Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern10(self, n):
    #     for i in range(1, n):
    #         print("*" * i)
    #     for i in range(n, 0, -1):
    #         print("*" * i)

    
    # Approach - 2

    # def pattern10(self, n):
    #     for i in range(1, n):
    #         print(f"{"*" * i}")
    #     for i in range(n, 0, -1):
    #         print(f"{"*" * i}")

    # Approach - 3

    def pattern10(self, n):
        for i in list(range(1, n)) + list(range(n, 0, -1)):
            print("*" * i)

# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern10(4)
'''
Factorial of a given number
-------------------------------------------------
You are given an integer n. Return the value of n! or n factorial.



Factorial of a number is the product of all positive integers less than or equal to that number.


Example 1

Input: n = 2

Output: 2

Explanation: 2! = 1 * 2 = 2.

Example 2

Input: n = 0

Output: 1

Explanation: 0! is defined as 1.

Constraints

0 <= n <= 10
'''

class Solution:
    
    def factorial(self, n) -> int:
        if n <= 1:
            return 1
        return (n * self.factorial(n-1))


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.factorial(5))
    print(sol.factorial(7))
    print(sol.factorial(4))
    print(sol.factorial(0))
    print(sol.factorial(2))
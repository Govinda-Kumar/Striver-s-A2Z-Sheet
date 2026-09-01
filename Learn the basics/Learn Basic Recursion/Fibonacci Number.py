'''
Fibonacci Number
-------------------------------------------------
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,



F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.


Given n, calculate F(n).


Example 1

Input : n = 2

Output : 1

Explanation : F(2) = F(1) + F(0) => 1 + 0 => 1.

Example 2

Input : n = 3

Output : 2

Explanation : F(3) = F(2) + F(1) => 1 + 1 => 2.

Constraints

0 <= n <= 20
'''

class Solution:

    # Approach - 1
    # def fib(self, n):
    #     if n == 0:
    #         return 0
    #     if n == 1: 
    #         return 1
    #     return self.fib(n-1) + self.fib(n-2)
            
    # Approach - 2
    def fib(self, n):
        if not hasattr(self, '_cache'):
            self._cache = {0: 0, 1: 1}
        
        if n in self._cache:
            return self._cache[n]
        self._cache[n] = self.fib(n-1) + self.fib(n-2)
        return self._cache[n]

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(0))
    print(sol.fib(1))
    print(sol.fib(2))
    print(sol.fib(3))
    print(sol.fib(8))
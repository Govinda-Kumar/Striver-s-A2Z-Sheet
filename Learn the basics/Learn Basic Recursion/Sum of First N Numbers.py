'''
Sum of First N Numbers
-------------------------------------------------
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Example 1

Input : N = 4

Output : 10

Explanation : first four natural numbers are 1, 2, 3, 4.

Sum is 1 + 2 + 3 + 4 => 10.

Example 2

Input : N = 2

Output : 3

Explanation : first two natural numbers are 1, 2.

Sum is 1 + 2 => 3.

Constraints

1 <= N <= 10^3
'''

class Solution:
    
    def NnumbersSum(self, N) -> int:
        if N == 0:
            return 0
        return (N + self.NnumbersSum(N-1))


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.NnumbersSum(5))
    print(sol.NnumbersSum(7))
    print(sol.NnumbersSum(4))
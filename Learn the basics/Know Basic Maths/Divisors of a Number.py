'''
Divisors of a Number
-------------------------------------------------
You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.



A number which completely divides another number is called it's divisor.


Example 1

Input: n = 6

Output = [1, 2, 3, 6]

Explanation: The divisors of 6 are 1, 2, 3, 6.

Example 2

Input: n = 8

Output: [1, 2, 4, 8]

Explanation: The divisors of 8 are 1, 2, 4, 8.

Constraints

0 <= n <= 1000

'''

class Solution:
    
    # Approach - 1
    # def divisors(self, n):
    #     result = []
    #     for i in range(1, n+1):
    #         if n % i == 0:
    #             result.append(i)
    #     print(result)
            
    # Approach - 2
    # def divisors(self, n):
    #     print([i for i in range(1, n+1) if n % i == 0])
    
    # Approach - 3
    def divisors(self, n):
        result = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                result.append(i)
                if n // i != i:
                    result.append(n // i)
            i += 1
        result.sort()
        print(result)


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.divisors(2)
    sol.divisors(83)
    sol.divisors(50)
    sol.divisors(12)
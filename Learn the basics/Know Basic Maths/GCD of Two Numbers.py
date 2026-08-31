'''
GCD of Two Numbers
-------------------------------------------------
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.



The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Example 1

Input: n1 = 4, n2 = 6

Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

Greatest Common divisor = 2.

Example 2

Input: n1 = 9, n2 = 8

Output: 1

Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.

Greatest Common divisor = 1.


Constraints

1 <= n1, n2 <= 1000
'''

class Solution:
    
    # Approach - 1
    # def GCD(self, n1, n2):
    #     greater = n1 if n1 - n2 >= 0 else n2
    #     smaller = n1 if n1 - n2 < 0 else n2
    #     for i in range(greater, 1, -1):
    #         if smaller % i == 0 and greater % i == 0:
    #             print(i)
    #             return 
    #     print(1)
            
    # Approach - 2
    def GCD(self, n1, n2):
        while n2:
            n1, n2 = n2, n1 % n2
        print(n1)
        


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.GCD(6, 12)
    sol.GCD(9, 8)
    sol.GCD(4, 6)
    sol.GCD(24, 36)
    sol.GCD(0, 5)
    sol.GCD(17, 13)
    sol.GCD(18, 48)
'''
Check for Prime Number
-------------------------------------------------
You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.



A prime number is a number which has no divisors except 1 and itself.


Example 1

Input: n = 5

Output: true

Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Example 2

Input: n = 8

Output: false

Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

Constraints

1 <= n <= 5000

'''

class Solution:
    
    # Approach - 1
    # def isPrime(self, n):
    #     if n == 1:
    #         return False
    #     for i in range(2, n):
    #         if n % i == 0:
    #             print(False)
    #             return
    #     print(True)
            
    # Approach - 2
    # def isPrime(self, n):
    #     print(n > 1 and all(n % i != 0 for i in range(2, n)))
    
    # Approach - 3
    def isPrime(self, n):
        if n <= 1: 
            print(False)
            return 
        if n <= 3: 
            print(True)
            return 
        if n % 2 == 0 or n % 3 == 0: 
            print(False)
            return
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                print(False)
                return
            i += 6
        print(True)


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.isPrime(2)
    sol.isPrime(3)
    sol.isPrime(83)
    sol.isPrime(50)
    sol.isPrime(12)
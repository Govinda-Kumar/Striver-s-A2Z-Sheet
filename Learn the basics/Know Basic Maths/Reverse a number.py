'''
Reverse a number
-------------------------------------------------
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.


Example 1

Input: n = 25

Output: 52

Explanation: Reverse of 25 is 52.

Example 2

Input: n = 123

Output: 321

Explanation: Reverse of 123 is 321.



Constraints

0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
'''

class Solution:
    
    # Approach - 1
    # def reverseNumber(self, n):
    #     c = ""
    #     while n >= 10:
    #         c += str(n % 10)
    #         n = n//10 
    #     print(c + str(n))
            
    # Approach - 2
    # def reverseNumber(self, n):
    #     print(str(n)[::-1])
        
    # Approach - 3
    # def reverseNumber(self, n):
    #     print("".join(reversed(str(n))))
    
    # Approach - 4 
    def reverseNumber(self, n):
        sign = -1 if n<0 else 1
        n = abs(n)
        reversed_num = 0
        while n>0:
            reversed_num = (reversed_num * 10) + (n % 10)
            n //= 10
        print(sign * reversed_num)


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.reverseNumber(103)
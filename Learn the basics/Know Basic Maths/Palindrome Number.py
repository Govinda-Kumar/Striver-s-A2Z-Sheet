'''
Palindrome Number
-------------------------------------------------
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.



A palindrome number is a number which reads the same both left to right and right to left.


Example 1

Input: n = 121

Output: true

Explanation: When read from left to right : 121.

When read from right to left : 121.

Example 2

Input: n = 123

Output: false

Explanation: When read from left to right : 123.

When read from right to left : 321.



Constraints

0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
'''

class Solution:
    
    # Approach - 1
    # def isPalindrome(self, n):
    #     inp = n
    #     c = ""
    #     while n >= 10:
    #         c += str(n % 10)
    #         n = n//10 
    #     reverse = c + str(n)
    #     print(reverse == str(inp))
            
    # Approach - 2
    # def isPalindrome(self, n):
    #     st = str(n)
    #     print(st[::-1] == st)
        
    # Approach - 3
    # def isPalindrome(self, n):
    #     print("".join(reversed(str(n))) == "".join(str(n)))
    
    # Approach - 4 
    def isPalindrome(self, n):
        if n < 0 or (n % 10 == 0 and n != 0):
            return False
        reversed_half = 0
        while n > reversed_half:
            reversed_half = (reversed_half * 10) + (n % 10)
            n //= 10
        print(n == reversed_half or n == reversed_half // 10)


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.isPalindrome(101)
    sol.isPalindrome(1011)
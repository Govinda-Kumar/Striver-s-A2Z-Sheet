'''
Count all Digits of a Number
-------------------------------------------------
You are given an integer n. You need to return the number of digits in the number.



The number will have no leading zeroes, except when the number is 0 itself.


Example 1

Input: n = 4

Output: 1

Explanation: There is only 1 digit in 4.

Example 2

Input: n = 14

Output: 2

Explanation: There are 2 digits in 14.



Constraints

0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
'''

class Solution:
    
    # Approach - 1
    # def countDigit(self, n):
    #     c = 1
    #     while n >= 10:
    #         c += 1
    #         n = n//10 
    #     print(c)
            
    # Approach - 2
    # def countDigit(self, n):
    #     print(len(str(n)))
    
    # Approach - 3
    def countDigit(self, n):
        if n == 0:
            print(1)
            return
        bits = n.bit_length()
        approx_digits = int(bits * 0.301)

        if n >= 10**approx_digits:
            approx_digits += 1
        print(approx_digits)


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.countDigit(100)
'''
Check if the Number is Armstrong
-------------------------------------------------
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.


An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


Example 1

Input: n = 153

Output: true

Explanation: Number of digits : 3.

13 + 53 + 33 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.

Example 2

Input: n = 12

Output: false

Explanation: Number of digits : 2.

12 + 22 = 1 + 4 = 5.

Therefore, it is not an Armstrong number.


Constraints

0 <= n <= 10^9

'''

class Solution:
    
    # Approach - 1
    # def isArmstrong(self, n):
    #     digits = 1
    #     num = n
    #     while num >= 10:
    #         digits += 1
    #         num //= 10
    #     num1 = n
    #     total = 0
    #     for i in range(digits):
    #         digit = num1 % 10
    #         total = total + digit**digits
    #         num1 //= 10
    #     print(total == n)
            
    # Approach - 2
    # def isArmstrong(self, n):
    #     s = str(n)
    #     length = len(s)
    #     total = sum(int(digit) ** length for digit in s)
    #     print(total == n)
    
    # Approach - 3
    def isArmstrong(self, n):
        s = str(n)
        length = len(s)
        lookup = [i ** length for i in range(10)]
        total = sum(lookup[int(digit)] for digit in s)
        print(total == n)


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.isArmstrong(612)
    sol.isArmstrong(153)
    sol.isArmstrong(2)
    sol.isArmstrong(370)
    sol.isArmstrong(1634)
    sol.isArmstrong(12)
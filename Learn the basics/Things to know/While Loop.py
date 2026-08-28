'''
While Loop
-----------------------------------------------------------------
Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.



A number ends with digit d if its last digit is d.


Example 1

Input: d = 1

Output: 12300

Explanation:

The first 50 positive integers ending with 1 are: 1, 11, 21, 31, ..., 491

Their sum is 12300.

Example 2

Input: d = 5

Output: 12500
'''

class Solution:
    def whileLoop(self, d : int) -> int:
        if d <= 0:
            return 0
        i = 1
        total = 0
        temp = d
        while(i <= 50):
            total += temp
            temp += 10
            i += 1
        return total

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.whileLoop(1))
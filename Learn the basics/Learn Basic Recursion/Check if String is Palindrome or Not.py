'''
Check if String is Palindrome or Not
-------------------------------------------------
Given a string s, return true if the string is palindrome, otherwise false.



A string is called palindrome if it reads the same forward and backward.


Example 1

Input : s = "hannah"

Output : true

Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Example 2

Input : s = "aabbaA"

Output : false

Explanation : The string when reversed is --> "Aabbaa", which is not same as original string, So we return false.

Constraints

1 <= s.length <= 10^3
s consist of only uppercase and lowercase English characters.
'''

class Solution:

    # Approach - 1
    # def palindromeCheck(self, s):
    #     def helper(left, right):
    #         if s[left] != s[right]:
    #             return False
    #         if left >= right:
    #             return True
    #         return helper(left + 1, right - 1)
    #     return helper(0, len(s)-1)
            
    # Approach - 2
    def palindromeCheck(self, s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return self.palindromeCheck(s[1: -1])

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.palindromeCheck("haonah"))
    print(sol.palindromeCheck("hanNNnah"))
    print(sol.palindromeCheck("hanNnah"))
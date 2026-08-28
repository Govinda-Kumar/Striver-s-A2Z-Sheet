'''
Switch Case
Subscribe to TUF+

Hints
Company
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

Ensure only the 1st letter of the answer is capitalised.

For printing use:-

for C++ : cout << variable_name;
for Java : System.out.print();
for Python : print()
for Javascript : console.log()

Example 1

Input: day = 3

Output: Wednesday

Example 2

Input: day = 8

Output: Invalid
'''

### NOTES: The match-case statement was introduced in Python 3.10 as a powerful structural pattern matching tool 

class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            case _:
                return "Invalid"
        

# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.whichWeekDay(8))
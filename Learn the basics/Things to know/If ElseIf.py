'''
If ElseIf
Subscribe to TUF+

Hints
Company
Given marks of a student, print on the screen:

Grade A if marks >= 90
Grade B if marks >= 70
Grade C if marks >= 50
Grade D if marks >= 35
Fail, otherwise.


For printing use:-

for C++ : cout << variable_name;
for Java : System.out.print();
for Python : print()
for Javascript : console.log()
for C# : Console.WriteLine();
for Go : fmt.Println()

Example 1

Input: marks = 95

Output: Grade A

Explanation: marks are greater than or equal to 90.

Example 2

Input: marks = 14

Output: Fail

Explanation: marks are less than 35.
'''

class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            return "Grade A"
        elif marks >=70:
            return "Grade B"
        elif marks >=50:
            return "Grade C"
        elif marks >=35:
            return "Grade D"
        else:
            return "Fail"


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.studentGrade(14))
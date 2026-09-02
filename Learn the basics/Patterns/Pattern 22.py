'''
Pattern 22
-------------------------------------------------
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5


Print the pattern in the function given to you.


Example 1

Input: n = 4

Output:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4


Example 2

Input: n = 2

Output:

2 2 2
2 1 2
2 2 2

Constraints

1 <= n <= 100
'''

class Solution:

    # Approach - 1

    # def pattern22(self, n):
    #     for i in range(n, 0, -1):
    #         for j in range(n, 0, -1):
    #             if j <= i:
    #                 print(i, end=" ")
    #             else:
    #                 print(j, end=" ")
    #         for k in range(2, n+1):
    #             if i >= k:
    #                 print(i, end=" ")
    #             else:
    #                 print(k, end=" ")
    #         print("")
    #     for i in range(2, n+1):
    #         for j in range(n, 0, -1):
    #             if j <= i:
    #                 print(i, end=" ")
    #             else:
    #                 print(j, end=" ")
    #         for k in range(2, n+1):
    #             if i >= k:
    #                 print(i, end=" ")
    #             else:
    #                 print(k, end=" ")
    #         print("")

    # Approach - 2

    # def pattern22(self, n):
    #     top_rows = []
    #     for i in range(n):
    #         left = [str(n - min(i, j)) for j in range(n)]
    #         full_row = left + left[-2::-1]
    #         top_rows.append(" ".join(full_row))
    #     final_box = top_rows + top_rows[-2::-1]
    #     print("\n".join(final_box))
        
        
    # Approach - 3
    
    def pattern22(self, n):
        cols = list(range(n, 0, -1)) + list(range(2, n + 1))
        rows = cols
        for r in rows:
            print(" ".join(str(max(r, c)) for c in cols))


# code runner
if __name__ == "__main__":
    sol = Solution()
    sol.pattern22(4)
    sol.pattern22(2)
    sol.pattern22(5)
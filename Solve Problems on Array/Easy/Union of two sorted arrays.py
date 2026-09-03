'''
Union of two sorted arrays
-------------------------------------------------
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Example 1

Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation:

The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2

Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

Output: [1, 3, 4, 5, 6, 7, 8, 9]

Explanation:

The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2

Constraints

1 <= nums1.length, nums2.length <= 1000
-10^4 <= nums1[i] , nums2[i] <= 10^4
Both nums1 and nums2 are sorted in non-decreasing order
'''
class Solution:
    # Approach - 1
    # def unionArray(self, nums1, nums2):
    #     result = nums1 + nums2
    #     result = list(set(result))
    #     result.sort()
    #     return result
    
    
    # Approach - 2
    # def unionArray(self, nums1, nums2):
    #     return list(set(nums1) | set(nums2))
    
    # Approach - 3
    def unionArray(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        result = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j += 1
            else: 
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1
                
        while i < n1:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        while j < n2:
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
        return result


# code runner
if __name__ == "__main__":
    sol = Solution()
    print(sol.unionArray([1, 2, 3, 4, 5],  [1, 2, 7]))
    print(sol.unionArray([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))
    print(sol.unionArray([1, 1, 2, 3, 3, 3, 6], [1, 1, 2, 3, 3, 3, 6]))
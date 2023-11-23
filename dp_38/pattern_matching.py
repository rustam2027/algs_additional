# https://leetcode.com/problems/regular-expression-matching/submissions/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matches = {}

        def recursion(i, j):
            if (i, j) in matches:
                return matches[(i, j)]  # If result is already known then return it

            if j == len(p):
                return i == len(s)  # If pattern string end check if string ends

            local_result = (i < len(s)) and (s[i] == p[j] or p[j] == '.')  # Check local result
            # If the string ends that doesn't mean that it false
            # There may be "*"

            if ((j + 1) < len(p)) and p[j + 1] == '*':
                # There two options:
                #  - "*" is nothing, then just skip it
                #  - "*" repeats, need to check for next char for this circumstances
                result = recursion(i, j + 2) or (local_result and recursion(i + 1, j))
            else:
                # If there no "*" then just check the next symbol
                result = local_result and recursion(i + 1, j + 1)

            matches[(i, j)] = result  # Save the result
            return result

        return recursion(0, 0)


A = Solution.isMatch(Solution, "ab", ".*")
print(A)

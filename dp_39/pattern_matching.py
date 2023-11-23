# https://leetcode.com/problems/wildcard-matching/submissions/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matches = {}

        def recursion(i, j):
            if (i, j) in matches:
                return matches[(i, j)]  # If result is already known then return it

            if j == len(p):
                return i == len(s)  # If pattern string end check if string ends

            local_result = (i < len(s)) and (s[i] == p[j] or p[j] == '?')  # Check local result
            # If the string ends that doesn't mean that it false
            # There may be "*"

            if p[j] == '*':
                # There two options:
                #  - "*" is nothing, then just skip it
                #  - keep "*" for the next char
                result = recursion(i, j + 1) or ((i < len(s)) and recursion(i + 1, j)) or (local_result and recursion(i + 1, j + 1))
            else:
                # If there no "*" then just check the next symbol
                result = local_result and recursion(i + 1, j + 1)

            matches[(i, j)] = result  # Save the result
            return result

        return recursion(0, 0)


print(Solution.isMatch(Solution, "acdcb", "a*c?b"))

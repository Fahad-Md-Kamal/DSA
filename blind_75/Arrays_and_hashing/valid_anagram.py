"""
# Valid Anagram
Easy Topics Company Tags Hints

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Example 1:

```py
Input: s = "racecar", t = "carrace"

Output: true
```

## Example 2:

```py
Input: s = "jar", t = "jam"

Output: false
```

Constraints:

`1 <= s.length, t.length <= 5 * 10^4`
`s` and `t` consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tmp_dict = {}
        for c in s:
            tmp_dict[c] = tmp_dict.get(c, 0) + 1
            
        for c in t:
            c_v = tmp_dict.get(c, 0)
            if c_v <= 0:
                return False
            tmp_dict[c] = c_v - 1
        return True
            

if __name__ == "__main__":
    solution = Solution()

    s = "racecar"
    t = "carrace"
    print(solution.isAnagram(s, t))  # Output: true
    
    s = "jar"
    t = "jam"
    print(solution.isAnagram(s, t))  # Output: false
        
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
        
        tmp_dict = dict()
        for ch in s:
            tmp_dict[ch] = tmp_dict.get(ch, 0) + 1
        
        for ch in t:
            val = tmp_dict.get(ch, 0)
            if val <= 0:
                return False
            tmp_dict[ch] = val - 1
        return sum(tmp_dict.values()) == 0
            

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aacc", "ccac", False),
    ]

    for idx, (s, t, expected) in enumerate(test_cases, start=1):
        result = solution.isAnagram(s, t)
        assert result == expected, (
            f"Test {idx} failed: s={s}, t={t}, expected={expected}, got={result}"
        )

    print(f"All tests passed: {len(test_cases)}")
        

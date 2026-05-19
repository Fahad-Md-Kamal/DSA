"""
# Group Anagrams
Medium Topics `Company Tags` Hints

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in **any order**.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

```py
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

**Example 2:**

```py
Input: strs = ["x"]

Output: [["x"]]
```

**Example 3:**

```py
Input: strs = [""]

Output: [[""]]
```

**Constraints:**

`1 <= strs.length <= 1000`.
`0 <= strs[i].length <= 100`
`strs[i]` is made up of lowercase English letters.
"""



from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = {}
        for word in strs:
            # 26-letter frequency signature ensures true anagram grouping.
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            key = tuple(freq)

            if key not in tmp_dict:
                tmp_dict[key] = []
            tmp_dict[key].append(word)
        return list(tmp_dict.values())


def canonical_groups(groups: List[List[str]]) -> List[List[str]]:
    return sorted(sorted(group) for group in groups)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["act", "pots", "tops", "cat", "stop", "hat"], [["act", "cat"], ["pots", "stop", "tops"], ["hat"]]),
        (["x"], [["x"]]),
        ([""], [[""]]),
        (["ab", "ba", "abc", "cab", "bca"], [["ab", "ba"], ["abc", "cab", "bca"]]),
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        (["a"], [["a"]]),
        (["aa", "aa", "aa"], [["aa", "aa", "aa"]]),
        (["ab", "aab", "baa"], [["ab"], ["aab", "baa"]]),
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
        (["zzz", "zz", "z"], [["zzz"], ["zz"], ["z"]]),
        (["listen", "silent", "enlist", "inlets"], [["listen", "silent", "enlist", "inlets"]]),
        (["rat", "tar", "art", "car"], [["rat", "tar", "art"], ["car"]]),
        (["aabb", "bbaa", "abab", "baba", "abba"], [["aabb", "bbaa", "abab", "baba", "abba"]]),
        (["abcd", "dcba", "lls", "sll", "sssll"], [["abcd", "dcba"], ["lls", "sll"], ["sssll"]]),
        (["qwe", "ewq", "weq", "abc", "bac", "cab"], [["qwe", "ewq", "weq"], ["abc", "bac", "cab"]]),
        (["anagram", "nagaram", "gramana", "hello"], [["anagram", "nagaram", "gramana"], ["hello"]]),
        (["ab", "bc", "cd", "de", "ef", "fe"], [["ab"], ["bc"], ["cd"], ["de"], ["ef", "fe"]]),
        (["", "", "a", "a"], [["", ""], ["a", "a"]]),
        (["abcabc", "cbacba", "aabbcc"], [["abcabc", "cbacba", "aabbcc"]]),
        (["noon", "onon", "nono", "oonn"], [["noon", "onon", "nono", "oonn"]]),
        (["xxy", "yxx", "xyx", "yyx"], [["xxy", "yxx", "xyx"], ["yyx"]]),
        (["mno", "nom", "omn", "pqr", "qrp"], [["mno", "nom", "omn"], ["pqr", "qrp"]]),
    ]

    for idx, (strs, expected) in enumerate(test_cases, start=1):
        actual = solution.groupAnagrams(strs)
        assert canonical_groups(actual) == canonical_groups(expected), (
            f"Test {idx} failed: strs={strs}, "
            f"expected={canonical_groups(expected)}, got={canonical_groups(actual)}"
        )

    print(f"All tests passed: {len(test_cases)}")

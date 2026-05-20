# https://neetcode.io/problems/string-encode-and-decode/question


from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_sen = ""
        for wrd in strs:
            enc_sen += f"{len(wrd)}#{wrd}"
        return enc_sen
        

    def decode(self, s: str) -> List[str]:
        words = []
        lp = 0
        while lp < len(s):
            rp = lp
            while rp < len(s) and s[rp] != "#":
                rp += 1
            length = int(s[lp:rp])
            lp = rp + 1
            words.append(s[lp:lp+length])
            lp = lp + length
        return words
            
            
        


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ["Hello", "World"],
        [],
        [""],
        ["", ""],
        ["a"],
        ["ab", "cd", "ef"],
        ["#", "##", "###"],
        ["12#34", "56", "#"],
        [" leading", "trailing ", " both "],
        ["one two", "three  four", "five"],
        ["!@#$", "%^&*()", "[]{}"],
        ["0", "00", "000"],
        ["same", "same", "same"],
        ["mixedCASE", "lower", "UPPER"],
        ["line1\nline2", "tab\tseparated"],
        ["বাংলা", "日本語", "emoji🙂"],
        ["long" * 50],
        ["a#b#c", "##middle##", "#end"],
        ["123", "0042", "9#9#9"],
        ["", "non-empty", "", "#", "42"],
    ]

    for idx, original in enumerate(test_cases, start=1):
        encoded = solution.encode(original)
        decoded = solution.decode(encoded)
        assert decoded == original, (
            f"Test {idx} failed: original={original}, encoded={encoded}, decoded={decoded}"
        )

    print(f"All tests passed: {len(test_cases)}")
    
    

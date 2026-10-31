class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alfabeto = [0] * 26
        for i in range(len(s)):
            alfabeto[ord(s[i]) - ord('a')] += 1
            alfabeto[ord(t[i]) - ord('a')] -= 1

        return all(letra == 0 for letra in alfabeto)
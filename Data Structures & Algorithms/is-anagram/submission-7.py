class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False

        alfabeto = [0] * 26

        for a, b in zip(s, t):
            alfabeto[ord(a) - ord('a')] += 1
            alfabeto[ord(b) - ord('a')] -= 1

        return all(letras == 0 for letras in alfabeto)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimS = "".join(c.lower() for c in s if c.isalnum())
        equivalente = 0

        for i in range(len(trimS) - 1, -1, -1):
            if trimS[i] == trimS[equivalente]:
                equivalente += 1
                continue
            else:
                return False
        return True    
            


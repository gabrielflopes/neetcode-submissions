class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimS = "".join(c.lower() for c in s if c.isalnum())
        equivalente, indice = 0, len(trimS) - 1

        while equivalente < indice:
            if trimS[indice] == trimS[equivalente]:
                equivalente += 1
                indice -= 1
                continue
            else:
                return False
        return True    
            


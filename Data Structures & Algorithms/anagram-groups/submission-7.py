class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = {}
        alfabeto = [0] * 26

        for palavra in strs:
            alfabeto [:] = [0] * 26    

            for letra in palavra:
                alfabeto[ord(letra) - ord('a')] += 1
            
            chave = tuple(alfabeto)
            
            if chave not in grupos:
                grupos[chave] = []
            grupos[chave].append(palavra)

        return list(grupos.values())
        
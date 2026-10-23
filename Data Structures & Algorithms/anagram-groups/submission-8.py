class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = defaultdict(list)
        alfabeto = [0] * 26

        for palavra in strs:
            alfabeto [:] = [0] * 26    

            for letra in palavra:
                alfabeto[ord(letra) - ord('a')] += 1
            
            grupos[tuple(alfabeto)].append(palavra)

        return list(grupos.values())
        
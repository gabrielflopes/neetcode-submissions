class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for palavra in strs:
            encoded_string += str(len(palavra)) + '#' + palavra
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs  = []
        i = 0

        while i < len(s):
            j = s.find('#', i)          
            tamanho = int(s[i:j])       
            palavra = s[j + 1 : j + 1 + tamanho]
            decoded_strs.append(palavra)
            i = j + 1 + tamanho     

        return decoded_strs 
        
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        contagem = {}
        
        for n in nums:
            contagem[n] = contagem.get(n, 0) + 1

        baldes = [[] for _ in range(len(nums) + 1)]
        for num, freq in contagem.items():
            baldes[freq].append(num)

        resultado = []
        for f in range(len(baldes) - 1, 0, -1):
            for num in baldes[f]:
                resultado.append(num)
                if len(resultado) == k:
                    return resultado

        return resultado
public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> anagramasAgrupados = new();
                
        foreach (string palavra in strs)
        {
            var alfabeto = new int[26];

            for (int i = 0; i < palavra.Length; i++)
            {
                alfabeto[palavra[i] - 'a']++;
            }
            string chave = string.Join(",", alfabeto);

            if (!anagramasAgrupados.ContainsKey(chave))
                anagramasAgrupados[chave] = new List<string>();

            anagramasAgrupados[chave].Add(palavra);
        }

        return anagramasAgrupados.Values.ToList();
    }    
}

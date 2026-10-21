public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> map = new();

        foreach (string palavra in strs)
        {
            int[] contagem = new int[26];
            foreach (char c in palavra)
                contagem[c - 'a']++;

            string etiqueta = string.Join(",", contagem);

            if (!map.ContainsKey(etiqueta))
                map[etiqueta] = new List<string>();

            map[etiqueta].Add(palavra);
        }

        return map.Values.ToList();
    }    
}

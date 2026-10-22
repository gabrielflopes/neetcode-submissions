public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
          return false;
        
        var alfabeto = new int[26];

        for (int i = 0; i < s.Length; i++)
        {
            alfabeto[s[i] - 'a']++;
            alfabeto[t[i] - 'a']--;
        }

        return alfabeto.All(c => c == 0);
    }
}

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        var alfabeto = new int[26];

        for (int i = 0; i < s.length(); i++)
        {
            alfabeto[s.charAt(i) - 'a']++;
            alfabeto[t.charAt(i) - 'a']--;
        }

        for (int qtdeLetra : alfabeto)
        {
            if (qtdeLetra != 0)
                return false;
        }

        return true;
    }
}

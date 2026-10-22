public class Solution {
    public bool hasDuplicate(int[] nums) {
        if (nums.Length <= 1)
            return false;
        
        HashSet<int> seen = new();

        foreach (var num in nums)
        {
            if (!seen.Add(num))
                return true;
        }

        return false;
    }
}
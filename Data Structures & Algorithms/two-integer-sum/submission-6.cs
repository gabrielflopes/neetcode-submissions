public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> seen = new();

        for (int i = 0; i < nums.Length; i++)
        {
            var diferenca = target - nums[i];

            if (seen.ContainsKey(diferenca))
                return new[] {seen[diferenca], i};

            seen.Add(nums[i], i);
        }

        return new int[0];
    }
}

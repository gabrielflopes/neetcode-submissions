public class Solution {
    public int[] TwoSum(int[] nums, int target) {      
        
        var seenBefore = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {            
            int faltante = target - nums[i];

            if (seenBefore.TryGetValue(faltante, out int indice))
                return new int[] {indice, i};

            seenBefore[nums[i]] = i;
        }    
        return new int[0];   
    }
}

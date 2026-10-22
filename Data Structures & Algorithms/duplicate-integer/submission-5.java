class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length <= 1)
            return false;

        var memoria = new HashSet();

        for (int num : nums)
        {
            if (!memoria.add(num))
                return true;

            memoria.add(num);    
        }

        return false;
    }
}
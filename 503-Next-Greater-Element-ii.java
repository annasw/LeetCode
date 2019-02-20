class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] nextGreaters = new int[nums.length];
        Arrays.fill(nextGreaters, -1); // prefill w/ -1 so we don't have to think about that later
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = (i+1) % nums.length; j != i; j = (j+1) % nums.length) { // cleverly abuse modulo operator so we don't have to thi-
                if (nums[j] > nums[i]) {
                    nextGreaters[i] = nums[j];
                    break; // break the (internal) for loop so w-
                }
            }
        }
        return nextGreaters; // this is it. what it's all been for. you're welcome, america.
    }
}

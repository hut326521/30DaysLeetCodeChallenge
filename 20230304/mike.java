/*
Use two pointer Algo to solve. Traverse all array and find valid temp-big subarray.
if meet invalid num, just record and start left pointer on next one. 
*/
class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        int n = nums.length;
        long ans = 0;
        int min = -1;
        int max = -1;
        int border = -1;
        
        for(int i = 0; i<n; i++) {
            if(nums[i] < minK || nums[i] > maxK){
                border = i;
            }
            
            if(nums[i] == minK){
                min = i;
            }
            
            if(nums[i] == maxK){
                max = i;
            }
            
            ans += Math.max(0, Math.min(min, max) - border);
        }
        
        return ans;
    }
}
/*
1. Find all of the continued 0.
2. Calculate all posible subarray by recursive.
*/
class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long ans = 0L;
        int count = 0;
        for(int i : nums){
            if(i == 0) {
                count++;
            } else if(count != 0) {
                ans += calFactorial(count);
                count = 0;
            }
        }
        ans += calFactorial(count);
        
        return ans;
    }
    
    long calFactorial(int num) {
        Long l= Long.valueOf(num);
        if(num < 1) {
            return 0L;
        }
        if(num == 1) {
            return 1L;
        }
        
        long calA = l*(l+1L)/2L;
        
        return calA;
    }
}
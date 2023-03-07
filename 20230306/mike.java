/*
Easy question which just count it to solve.
Enumerate 3 conditions(kth in start, mid, end) and return it.
Time Complexity: O(N)
Space Complexity: O(1)
*/
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int gap = k;
        if(arr[0] != 1) {
            gap -= (arr[0] - 1);
        }

        if(gap <= 0) {
            return k;
        }

        for(int i = 1; i < arr.length; i++) {
            int distance = arr[i] - arr[i-1];
            if(distance != 1){
                gap -= (distance - 1);
            }

            if(gap <= 0) {
                return arr[i] + gap - 1;
            }
        }

        return arr[arr.length - 1] + gap;
    }
}
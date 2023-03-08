/*
Use Binary Search to solve it, just same as recent daily questions.
left can be 0 or 1, right could be max(piles) because 1 hour can only eat 1 stack.

Edge case need to be careful:
1. piles's length = 1 or 2
*/
class Solution {
    int[] mPiles;
    int mH;

    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        mPiles = piles;
        mH = h;
        int left = 0;
        int right = piles[piles.length-1];
        if(left == right) {
            int sum = 0;
            for(int a: piles) {
                sum+=a;
            }

            if(sum % h == 0) {
                return sum/h;
            } else {
                return (sum/h)+1;
            }
        }

        while(left + 1 != right){
            int mid = left + (right - left)/2;

            if(eatTimeByCurSpeed(mid) <= h){
                right = mid;
            } else {
                left = mid;
            }
        }

        return right;
    }

    int eatTimeByCurSpeed(int speed){
        int res = 0;
        for(int i : mPiles){
            if(i % speed == 0) {
                res += ((i/speed));
            } else {
                res += ((i/speed) + 1);
            }

            if(res > mH) {
                return res;
            }
        }

        return res;
    }
}
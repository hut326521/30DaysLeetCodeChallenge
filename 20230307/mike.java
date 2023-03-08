/*
Just Binary Search.
Use min timeVal as left(to reduce spending time),
and (min timeVal)*totalTrips as right(it must be bigger than answer).
That's why sort array. It may return value earlier in calCurTimeToTripAmount() as well.

Note: We need to search left and right in type long variable. 
Because Integer will overflow(ans's type is long...)
*/
class Solution {
    int[] busTime;
    int mTotalTrips;

    public long minimumTime(int[] time, int totalTrips) {
        Arrays.sort(time);
        
        Long lTime = new Long(time[0]);
        Long ltotalTrips = new Long(totalTrips);
        
        if(time.length == 1) {
            return lTime * ltotalTrips;
        }
        
        busTime = time;
        mTotalTrips = totalTrips;
        long left = 0;
        long right = lTime * totalTrips;

        while(left + 1 != right) {
            long mid = left + (right - left)/2;
            if(calCurTimeToTripAmount(mid) < totalTrips) {
                left = mid;
            } else {
                right = mid;
            }
        }

        return right;
    }

    int calCurTimeToTripAmount(long curTime){
        int res = 0;
        for (int j : busTime) {
            res += curTime / j;

            if (res > mTotalTrips) {
                return res;
            }
        }
        return res;
    }
}
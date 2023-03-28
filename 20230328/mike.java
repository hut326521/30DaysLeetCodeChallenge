class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int allDays = days[days.length - 1];
        int[] memo = new int[allDays + 1];
        List<Integer> daysList = new ArrayList<>();
        for(int d : days) {
            daysList.add(d);
        }

        // Days[] contain 1 to 365.
        memo[0] = 0;
        for(int i = 1; i <= allDays; i++) {
            if(!daysList.contains(i)) {
                memo[i] = memo[i-1];
            } else {
                int tempMinimal = Integer.MAX_VALUE;
                tempMinimal = Math.min(tempMinimal, memo[i-1] + costs[0]);
                if (i > 6) {
                    tempMinimal = Math.min(tempMinimal, memo[i-7] + costs[1]);
                } else {
                    tempMinimal = Math.min(tempMinimal, memo[0] + costs[1]);
                }
                if (i > 29) {
                    tempMinimal = Math.min(tempMinimal, memo[i-30] + costs[2]);
                } else {
                    tempMinimal = Math.min(tempMinimal, memo[0] + costs[2]);
                }
                memo[i] = tempMinimal;
            }
        }
        return memo[allDays];
    }
}

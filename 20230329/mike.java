/*
Optimal version.
*/
class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        // Process the dish to increasing order.
        Arrays.sort(satisfaction);

        int positiveSum = 0;
        int positiveTempSum = 0;
        int negativeSum = 0;
        int negativeTempSum = 0;
        for(int i = satisfaction.length-1; i >= 0; i--) {
            if(satisfaction[i] >= 0) {
                positiveTempSum += satisfaction[i];
                positiveSum += positiveTempSum;
            } else {
                negativeTempSum += satisfaction[i];

                if(positiveTempSum > Math.abs(negativeTempSum)) {
                    positiveSum += positiveTempSum;
                    negativeSum += negativeTempSum;
                } else {
                    break;
                }
            }
        }
        return positiveSum + negativeSum;
    }
}

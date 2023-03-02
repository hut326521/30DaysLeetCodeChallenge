/* 443. String Compression
Due to the requirement of Question(uses only constant extra space),
I decide to use Two Pointer Algo to solve.

Time complexity: O(chars.length)
Space complexity: O(1)
*/
class Solution {
    public int compress(char[] chars) {
        if(chars.length == 1) {
            return 1;
        }
        
        int curr = 0;
        int bossPointer = 0;
        int searchPointer = 0;
        int len = chars.length;

        while(bossPointer < len){
            while(searchPointer < len && chars[searchPointer] == chars[bossPointer]){
                searchPointer++;
            }

            chars[curr++] = chars[bossPointer];
            int count = (searchPointer - bossPointer);

            if(count > 1) {
                char[] countChar = String.valueOf(count).toCharArray();

                for (char c : countChar){
                    chars[curr++] = c;
                }
            }
            
            bossPointer = searchPointer;
        }

        return curr;
    }
}
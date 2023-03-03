/*
There are 3 ways to solve this problem:
1. bulid-in function - string.indexof()
2. KMP Algo
3. Bruto Force - Find all needle[0] in haystack then start compare.

Bruto Force don't cause TLE so that we solve by this way.
Need to catch up KMP Algo in the future.
*/
class Solution {
    public int strStr(String haystack, String needle) {
        int comparePointer = 0;

        if(haystack.length() < needle.length()){
		    return -1;
	    }

        for(int i = 0; i < haystack.length(); i++){
            if(haystack.charAt(i) == needle.charAt(comparePointer)){
                while(comparePointer < needle.length() && ((comparePointer + i) < haystack.length())){
                    if(haystack.charAt(i+comparePointer) != needle.charAt(comparePointer)){
                        comparePointer = 0;
						break;
					} else {
						comparePointer++;
					}
                }

		        if(comparePointer == needle.length()){
		            return i;
		        }
            }
        }

        return -1;
    }
}

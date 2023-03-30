class Solution {
    public boolean isScramble(String s1, String s2) {
        int stringLen = s1.length();

        if((stringLen == 1) && s1.equals(s2)) {
            return true;
        }

        if (s1.contains(s2)) {
            return true;
        }

        if(!isSameCharGroup(s1, s2)) {
            return false;
        }

        if(s1.charAt(0) == s2.charAt(0)){
            for(int i = 1; i < stringLen; i++) {
                if(!(s1.charAt(i) == s2.charAt(i))) {
                    return isScramble(s1.substring(i, stringLen), s2.substring(i, stringLen));
                }
            }
        } else if (s1.charAt(0) == s2.charAt(stringLen-1)){
            for(int i = 1; i < stringLen; i++) {
                if(!(s1.charAt(i) == s2.charAt(stringLen - i - 1))) {
                    return isScramble(s1.substring(i, stringLen), s2.substring(0, stringLen - i));
                }
            }
        } else if (s1.charAt(stringLen-1) == s2.charAt(0)){
            for(int i = 1; i < stringLen; i++) {
                if(!(s2.charAt(i) == s1.charAt(stringLen - i - 1))) {
                    return isScramble(s2.substring(i, stringLen), s1.substring(0, stringLen - i));
                }
            }
        } else if (s1.charAt(stringLen-1) == s2.charAt(stringLen-1)){
            for(int i = stringLen-2; i >0; i--) {
                if(!(s1.charAt(i) == s2.charAt(i))) {
                    return isScramble(s1.substring(0, i+1), s2.substring(0, i+1));
                }
            }
        }


        boolean ans = false;
        for (int spIndex = 1; spIndex < stringLen; spIndex++) {
            String s1left = s1.substring(0, spIndex);
            String s1right = s1.substring(spIndex, stringLen);
            String s2left = s2.substring(0, spIndex);
            String s2right = s2.substring(spIndex, stringLen);
            String s2leftReverse = s2.substring(0, stringLen - spIndex);
            String s2rightReverse = s2.substring(stringLen - spIndex, stringLen);

            if(isSameCharGroup(s1left, s2left) && isSameCharGroup(s1right, s2right)) {
                ans = (isScramble(s1right, s2right) && isScramble(s1left, s2left));
            }

            if(ans) {
                return true;
            }

            if(isSameCharGroup(s1left, s2rightReverse) && isSameCharGroup(s1right, s2leftReverse)) {
                ans = (isScramble(s1left, s2rightReverse) && isScramble(s1right, s2leftReverse));
            }

            if(ans) {
                return true;
            }
        }

        return false;
    }

    boolean isSameCharGroup(String s1, String s2){
        for(char c : s1.toCharArray()) {
            if(s2.indexOf(c) < 0) {
                return false;
            }
        }

        return true;
    }
}
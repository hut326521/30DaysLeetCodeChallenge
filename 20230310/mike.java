/*
The key point is how to get random node in LinkedList(Can't use index to access it).
So every time we search next node(soppose Nth node), 
we decide whether pick this val in 1/n possibility.
So it has (n-1)/n possibility to keep origin val.
Because (1/2)*(2/3)*(3/4)*...*((n-1)/n) = 1/n, 
then all of the node will have the same possibility to be chosen.

This shall pass the follow-up cases(don't need additional space.)
*/
class Solution {
    ListNode mHead;
    ListNode mInitHead;
    Random mRand = new Random();
    int ans;
    
    public Solution(ListNode head) {
        mInitHead = head;
    }
    
    public int getRandom() {
        mHead = mInitHead;
        int count = 0;
        ans = ans = mHead.val;
        
        while(mHead != null) {
            count++;
            int curRandNum = mRand.nextInt(count);
            
            if(curRandNum == 1) {    
                ans = mHead.val;
            }
            
            mHead = mHead.next;
        }
        
        return ans;
    }
}
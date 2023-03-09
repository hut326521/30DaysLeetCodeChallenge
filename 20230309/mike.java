/*
Basic solution by HashSet. Easy.
*/
public class Solution {
    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> mNote = new HashSet<>();

        while(head != null){
            if(!mNote.contains(head)) {
                mNote.add(head);
            } else {
                return head;
            }
            head = head.next;
        }

        return null;
    }
}

/*
Advanced solution(space cose O(1))
*/
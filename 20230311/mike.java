/*
Use slow and fast pointer to find mid node(just like recent questions).
If we find mid node, cut it into two part as left subtree and right subtree.
*/
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head==null) {
            return null;
        }
        
        return findRootNodeInMid(head,null);
    }
    
    public TreeNode findRootNodeInMid(ListNode head, ListNode tail){
        ListNode slow = head;
        ListNode fast = head;
        
        if(head==tail) {
            return null;
        }
    
        while(fast!=tail&&fast.next!=tail){
            fast = fast.next.next;
            slow = slow.next;
        }
        
        TreeNode mid = new TreeNode(slow.val);
        
        mid.left = findRootNodeInMid(head,slow);
        mid.right = findRootNodeInMid(slow.next,tail);
        
        return mid;
    }
}
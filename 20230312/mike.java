/*
Just like the concept of MergeSort.
Partition every node and let it merge in increased.
After merge all node, return it.
Tomorrow I'll see other way to solve this problem, but I don't have energy to do this know.
*/
class Solution {
    public static ListNode mergeKLists(ListNode[] lists){
        return partion(lists,0,lists.length-1);
    }

    public static ListNode partition(ListNode[] lists,int start,int end){
        if(start==end) {
            return lists[start];
        }
        
        if(start < end) {
            int q=(start+end)/2;
            ListNode l1 = partition(lists,start,q);
            ListNode l2 = partition(lists,q+1,end);
            
            return merge(l1,l2);
        } else{
            return null;
        }
    }

    public static ListNode merge(ListNode l1,ListNode l2){
        if(l1==null) {
            return l2;
        }
        
        if(l2==null) {
            return l1;
        }
        
        if(l1.val < l2.val) {
            l1.next = merge(l1.next,l2);
            return l1;
        } else {
            l2.next = merge(l1,l2.next);
            return l2;
        }
    }
}
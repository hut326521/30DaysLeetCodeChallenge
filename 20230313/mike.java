/*
Solved it by DFS. Compare two nodes(left node's right and right node's left.).
Try to find illegal cases.
There are 3 possible cases:
1. Both are null: end traverse and return true.
2. One is null or value not equal: end traverse and return false.
3. Both are not null and have equal values: continue traversing.
*/
class Solution {

    public boolean isSymmetric(TreeNode root) {
        return isMirrorTree(root.left, root.right);
    }
    
    boolean isMirrorTree(TreeNode r1, TreeNode r2) {
        if(r1 == null && r2 == null) {
            return true;
        }
        
        if(r1 == null || r2 == null) {
            return false;
        }
        
        if(r1.val != r2.val) {
            return false;
        }
        
        return isMirrorTree(r1.right, r2.left) 
            && isMirrorTree(r1.left, r2.right);
    }
}
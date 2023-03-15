/*
Traverse by BFS.
If null node is found more than one time, it must not be completely tree.
Easy way to solve it by BFS.
*/
class Solution {
    Queue<TreeNode> mQ = new LinkedList<>();
    boolean isNullNodeExisted = false;
    
    public boolean isCompleteTree(TreeNode root) {
        mQ.offer(root);
        
        while(!mQ.isEmpty()) {
            TreeNode tempNode = mQ.poll();

            if(tempNode == null) {
                isNullNodeExisted = true;
                
                continue;
            }
            
            if(isNullNodeExisted) {
                return false;
            }
            
            mQ.offer(tempNode.left);
            mQ.offer(tempNode.right);
        }
        
        return true;
    }
}
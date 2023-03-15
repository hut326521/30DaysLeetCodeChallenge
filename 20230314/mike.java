/*
Easily solved by DFS.
*/
class Solution {
    int res = 0;

    public int sumNumbers(TreeNode root) {
        dfs(root, 0);
        return res;
    }

    void dfs(TreeNode root, int curNodeSum) {
        if(root == null) {
            return;
        }

        curNodeSum = (curNodeSum * 10) + root.val;

        if(root.left == null && root.right == null) {
            res += curNodeSum;
        }

        dfs(root.left, curNodeSum);
        dfs(root.right, curNodeSum);
    }
}
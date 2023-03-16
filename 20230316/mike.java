/*
I don't like this kind of question because it seldom appears except for exam of CS Master.
Step 1. Use postOrder[last] as root, find root's index in inorder.
Step 2. Use dfs to find root.left and root.right(input left subTree and right subTree.)
Step 3. Repeat above steps.
*/
class Solution {
    HashMap<Integer, Integer> mInorderMap = new HashMap<>();
    int[] mInorder;
    int[] mPostorder;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        for (int i = 0; i < inorder.length; i++) {
            mInorderMap.put(inorder[i], i);
        }

        mInorder = inorder;
        mPostorder = postorder;

        return buildTree(0, inorder.length - 1, 0, postorder.length - 1);
    }

    TreeNode buildTree(int inOrderStart, int inOrderEnd, int postOrderStart, int postOrderEnd) {
        if((inOrderStart > inOrderEnd) || (postOrderStart > postOrderEnd)) {
            return null;
        }

        int rootValueInInorder = mPostorder[postOrderEnd];
        int rootIndexInInorder = mInorderMap.getOrDefault(rootValueInInorder, 0);

        TreeNode root = new TreeNode(rootValueInInorder);

        int leftSubTreeSize = rootIndexInInorder - inOrderStart;
        int rightSubTreeSize = inOrderEnd - rootIndexInInorder;

        root.left = buildTree(inOrderStart, rootIndexInInorder - 1, postOrderStart, postOrderStart + leftSubTreeSize - 1);
        root.right = buildTree(rootIndexInInorder + 1, inOrderEnd, postOrderEnd - rightSubTreeSize, postOrderEnd - 1);

        return root;
    }
}
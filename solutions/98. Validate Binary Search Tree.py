class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorderCheck(root: TreeNode, lower: float, upper: float) -> bool:
            if root == None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            else:
                return inorderCheck(root.left, lower, root.val) and inorderCheck(root.right, root.val, upper)
        
        
        return inorderCheck(root, float('-inf'), float('inf'))
​

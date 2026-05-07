# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        # inorder is left node right
        ret = []
        # i think u have to do recursive

        def dfs(node):
            if not node:
                return
            
            if node.left:
                dfs(node.left)

            ret.append(node.val)

            if node.right:
                dfs(node.right)
            
        dfs(root)
        return ret
        

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        # inorder is left node right
        ret = []
        #iterative solution
        stack = []
        cur = root
        while stack or cur:
            while cur:
                # add parents to stack
                stack.append(cur)
                # go down to the very left
                cur = cur.left
            # add left most node to ret
            node = stack.pop()
            ret.append(node.val)

            # add the right nodes
            cur = node.right
        return ret
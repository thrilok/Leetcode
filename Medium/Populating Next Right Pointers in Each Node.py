"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        row = 0
        current_row = 0
        if root == None:
            return root
        stack = [root]
        while len(stack) >0:
            current_row +=1
            current = stack.pop(0)
            if current.left != None:
                stack.append(current.left)
            if current.right != None:
                stack.append(current.right)
            if current_row == 2**row:
                current_row = 0
                row += 1
            else:
                current.next = stack[0]
        return root
    
# Runtime: 72 ms, faster than 18.26% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.7 MB, less than 13.01% of Python3 online submissions for Populating Next Right Pointers in Each Node.


"""
Recursive approach and follow up question with space as O(1) and time complexity as O(n)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.recursiveConnect(root, root)
        return root
        
    def recursiveConnect(self, current, parent):
        if parent.left == current:
            current.next = parent.right
        elif parent.right == current:
            if parent.next == None:
                current.next = None
            else:
                current.next = parent.next.left
        if current.left != None:
            self.recursiveConnect(current.left, current)
        if current.right != None:
            self.recursiveConnect(current.right, current)

# Runtime: 64 ms, faster than 54.89% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.5 MB, less than 51.31% of Python3 online submissions for Populating Next Right Pointers in Each Node.


""" Java solution
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null)
            return null;
        recursiveConnect(root, root);
        return root;
    }
    
    public static void recursiveConnect(Node current, Node parent) {
        if (parent.left == current) current.next = parent.right;
        else if (parent.right == current){
             if (parent.next == null) current.next = null;
            else current.next = parent.next.left;
        }
         if (current.left != null)
            recursiveConnect(current.left, current);
        if (current.right != null)
            recursiveConnect(current.right, current);
        return;
    }
}

# Runtime: 0 ms, faster than 100.00% of Java online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 39 MB, less than 82.33% of Java online submissions for Populating Next Right Pointers in Each Node.
"""

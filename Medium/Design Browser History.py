class BrowserHistory:
    def __init__(self, homepage: str):
        self.root = Node(homepage)
    
    def visit(self, url: str) -> None:
        node = Node(url)
        node.previous = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        count = 0
        while self.root.previous and count <steps:
            self.root = self.root.previous
            count+=1
        return self.root.val
    def forward(self, steps: int) -> str:
        count = 0
        while self.root.next and count <steps:
            self.root = self.root.next
            count+=1
        return self.root.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.previous = None

# Runtime: 356 ms, faster than 44.02% of Python3 online submissions for Design Browser History.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Design Browser History.

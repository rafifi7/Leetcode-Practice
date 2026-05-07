class Node:
    def __init__(self, val: str):
        self.prev = None
        self.next = None
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        self.head = self.curr
        self.tail = self.curr
        self.backSteps = 0
        self.forSteps = 0

    def visit(self, url: str) -> None:
        newNode = Node(url)
        # this means that the head is now null because the forward history is now lsot
        # attach curr to newNode
        newNode.prev = self.curr
        self.curr.next = newNode
        # update global head and curr ptr
        self.head = newNode
        self.curr = self.head

        # update steps
        self.forSteps = 0
        self.backSteps += 1

    def back(self, steps: int) -> str:
        # if steps larger than backward steps
        if steps >= self.backSteps:
            self.curr = self.tail
            self.forSteps += self.backSteps
            self.backSteps = 0
            return self.curr.val
        
        
        for i in range(steps):
            self.curr = self.curr.prev

        # update steps
        self.forSteps += steps
        self.backSteps -= steps

        return self.curr.val

    def forward(self, steps: int) -> str:
        # if steps larger than backward steps
        if steps >= self.forSteps:
            self.curr = self.head
            self.backSteps += self.forSteps
            self.forSteps = 0
            return self.curr.val
        
        # else
        for i in range(steps):
            self.curr = self.curr.next

        # update steps
        self.forSteps -= steps
        self.backSteps += steps

        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# first example
# leetcode homepage
# visit google
# visit facebook
# visit youtube
# curr at yt  go back 1
# back to facebook but tail is still at yt
# visit linkedin
# forward 2 but since we visited, 
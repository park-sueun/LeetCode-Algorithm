class Homepage:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = Homepage(homepage)
        self.curr = self.head

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_url = Homepage(url)
        self.curr.next = new_url
        new_url.prev = self.curr
        self.curr = new_url
    

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.curr.prev is None:
                break
            self.curr = self.curr.prev
            
        return self.curr.url
        
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.curr.next is None:
                break
            else:
                self.curr = self.curr.next
            
        return self.curr.url
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 반자르고 짝수인 경우는 그대로, 홀수인 경우는 중간 숫자 제거
        # 앞에 잘라진 것들은 스택으로 쌓고
        # 나머지는 for문 돌면서 스택 pop하여 비교
        # 만약 pop한 갚과 다르면 false
        # 다 돌았을 때 true
        
        x = list(str(x))
        left, right = x[:len(x)/2], x[len(x)/2:]
        if len(left) != len(right):
            right.pop(0)
            
        for r in right:
            if r != left.pop():
                return False
            
        return True
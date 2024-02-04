class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        answer = []
        stack = [] # [(idx, temperature)]
        for idx, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                s = stack.pop()
                answer.append((s[0], idx - s[0]))
            stack.append((idx, val))
        
        # stack에 남은 온도는 따뜻해지는 날을 찾지 못한 것이므로 0으로 표기
        while stack:
            s = stack.pop()
            answer.append((s[0], 0))
        
        # index 번호로 정렬
        sorted_answer = sorted(answer, key=lambda x: x[0])
        return [answer[1] for answer in sorted_answer]
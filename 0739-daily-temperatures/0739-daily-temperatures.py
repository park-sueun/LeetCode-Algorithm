class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        answer = [0] * len(temperatures)
        stack = [] # [(idx, temperature)]
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and stack[-1][1] < curr_temp:
                prev_day, _ = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append((curr_day, curr_temp))

        return answer
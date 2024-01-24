class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        result = []
        temp = []
        for idx, val in enumerate(temperatures):
            if temp == [] or temp[-1][1] >= val:
                temp.append((idx, val))
            else:
                while temp:
                    if temp[-1][1] < val:
                        t = temp.pop()
                        result.append((t[0], idx - t[0]))
                    else:
                        break
                temp.append((idx, val))
                
        for t in temp:
            result.append((t[0], 0))
        
        return [t[1] for t in sorted(result, key=lambda x: x[0])]

                
                
            
        
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = (1, height[0])
        right = (len(height), height[len(height)-1])
        
        while left[0] < right[0]:
            lx, ly = left
            rx, ry = right
            if lx >= rx:
                break
            
            curr_area = (rx - lx) * min(ry, ly)
            if max_area < curr_area:
                max_area = curr_area
            
            if ly < ry:
                curr_y = ly
                while lx < len(height) and height[lx] <= curr_y:
                    lx += 1
                
                left = (lx+1, height[lx])
            else:
                curr_y = ry
                while rx > 0 and height[rx-1] <= curr_y:
                    rx -= 1
                    
                right = (rx, height[rx-1])
            
        return max_area
class Solution:
    def maxArea(self, height: List[int]) -> int:
            head_idx = 0 
            tail_idx = len(height) - 1

            max_area = 0
            while head_idx < tail_idx:
                curr_area = min(height[head_idx], height[tail_idx]) * (tail_idx - head_idx)
                if curr_area > max_area:
                    max_area = curr_area

                if height[head_idx] > height[tail_idx]:
                    tail_idx -= 1
                else:
                    head_idx += 1  
                    
            return max_area

                
            

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        locked = [0] * len(temperatures)
        tentative = [] # stack 

        hotter = True

        for index, temp in enumerate(temperatures):

            while tentative and hotter:
                if temp > tentative[-1][0]:
                    final_index = index - (tentative[-1])[1]
                    locked[(tentative[-1])[1]] = final_index
                    tentative.pop()
                else:
                    hotter = False
                    tentative.append((temp, index))
            
            tentative.append((temp, index))
            hotter = True
        
        return locked
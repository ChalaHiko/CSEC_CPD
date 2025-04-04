class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                if heights[j] >= heights[i]:
                    heights[j], heights[i] =  heights[i],  heights[j]
                    names[j], names[i] =  names[i],  names[j] 
        return names

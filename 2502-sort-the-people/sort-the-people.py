class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            min=i
            for j in range(i+1,len(heights)):
                if heights[min]<heights[j]:
                    min=j
            heights[i],heights[min]=heights[min],heights[i]
            names[i],names[min]=names[min],names[i]
        return names
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            key1 = heights[i]
            key2 = names[i]
            j = i - 1

            while j >= 0 and heights[j] < key1:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = key1 
            names[j + 1] = key2
        
        return names
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def flip(arr):
            s=0
            e=len(arr)-1
            while s <= e:
                arr[s],arr[e] = arr[e],arr[s]
                s+=1
                e-=1
            return arr
        def invert(arr):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
            return arr

        for i in range(len(image)):
            flip(image[i])
            invert(image[i])

        return image
        

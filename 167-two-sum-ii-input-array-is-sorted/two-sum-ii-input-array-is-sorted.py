class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k=[]
        for i in range(len(numbers)):
            r=target-numbers[i]
            low=i+1
            high=len(numbers)-1
            while(low<=high):
                mid=(high+low)//2
                if numbers[mid]==r:
                    k.append(i+1)
                    k.append(mid+1)
                    break
                elif numbers[mid]<r:
                    low=mid+1
                else:
                    high=mid-1
        return k
        
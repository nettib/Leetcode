class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        notConsistent = 0
        for index in range(len(words)):
            word = words[index]
            for i in range(len(word)):
                if word[i] not in allowed:
                    notConsistent += 1
                    break
        return len(words) - notConsistent
           
       

        
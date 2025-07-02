class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            count[sortedS].append(s)

        return list(count.values())
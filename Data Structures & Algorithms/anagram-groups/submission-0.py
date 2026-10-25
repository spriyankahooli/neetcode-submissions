class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for word in strs:
            sword = str(sorted(word))
            map1[sword].append(word)
        return list(map1.values())
        
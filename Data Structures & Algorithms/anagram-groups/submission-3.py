class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for word in strs:
            map1[str(sorted(word))].append(word)
        return list(words for words in map1.values())
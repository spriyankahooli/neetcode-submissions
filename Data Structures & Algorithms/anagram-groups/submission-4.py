class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            anagram[str(sorted(word))].append(word)
        return list(words for words in anagram.values())
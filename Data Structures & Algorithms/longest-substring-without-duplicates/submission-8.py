class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen ={}
        maxlen =0 
        left = 0 
        for right,char in enumerate(s):
            if char in seen and seen[char]>= left:
                left = seen[char]+1
            seen[char]= right 
            maxlen = max(maxlen,(right-left+1))
        return maxlen
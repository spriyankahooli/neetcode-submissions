class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right =0,0
        maxlen =0
        numrep =0
        highf =0
        seen={}
        while right< len(s):
            seen[s[right]] = seen.get(s[right], 0) + 1
            highf = max(highf, seen[s[right]])
            numrep = (right-left)+1- highf

            if numrep > k:
                seen[s[left]]-=1
                left+=1
            maxlen = max(maxlen, (right-left)+1)
            right+=1
        return maxlen
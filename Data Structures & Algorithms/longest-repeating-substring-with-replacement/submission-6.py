class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0 
        numrep =0
        maxlen =0
        seen ={}
        highf =0

        for right, char in enumerate(s):
            seen[char]= seen.get(char,0)+1
            highf = max(highf,seen[char])
            numrep = (right-left)+1 -highf

            if numrep>k:
                seen[s[left]]-=1
                left+=1
            maxlen=max(maxlen,(right-left)+1)
        return maxlen

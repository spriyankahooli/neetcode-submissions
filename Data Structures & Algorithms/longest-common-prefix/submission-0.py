class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l = strs[0]
        r = strs[-1]
        res =[]
        for i in range(min(len(l),len(r))):
            if l[i] != r[i]:
                break
            res.append(l[i])
        return ''.join(res)
        
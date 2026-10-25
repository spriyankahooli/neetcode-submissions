class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 =len(s1),len(s2)
        if n1>n2:
            return False 
        target = Counter(s1)
        window = Counter(s2[:n1])
        if target == window:
            return True 
        for i in range(n1,n2):
            window[s2[i]]+=1
            window[s2[i-n1]]-=1
            if window[s2[i-n1]]==0:
                del window[s2[i-n1]]
            if window ==target:
                return True 
        return False 

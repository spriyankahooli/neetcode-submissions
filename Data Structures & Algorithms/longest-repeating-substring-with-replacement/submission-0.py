class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right =0,0
        high_frq= 0
        map1= {}
        max_len =0
        while right < len(s):
            map1[s[right]] = map1.get(s[right],0)+1
            high_frq = max(high_frq, map1[s[right]])

            num_char_replac = (right-left+1)- high_frq
            if num_char_replac > k:
                map1[s[left]]-=1
                left+=1
            max_len = right-left+1
            right+=1
        return max_len        
        
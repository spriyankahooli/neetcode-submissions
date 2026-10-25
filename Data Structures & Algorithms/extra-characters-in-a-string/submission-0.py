class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        d_set = set(dictionary)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for j in range(i, n):
                word = s[i:j + 1]
                if word in d_set:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]
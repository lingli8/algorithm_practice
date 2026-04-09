class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s):
                    if s[i:i+len(w)] == w:
                        if dp[i+len(w)]: # i过来的那个点是否存在,只有为true即存在的时候才行
                            dp[i] = True
                            break
        return dp[0]
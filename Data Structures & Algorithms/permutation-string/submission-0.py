class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        s1_count = [0] * 26
        window_count = [0] * 26
        if k > n:
            return False
        for i in range(k):
            s1_count[ord(s1[i])- ord('a')] += 1
            window_count[ord(s2[i])- ord('a')] += 1
        if s1_count == window_count:
            return True
        for i in range(k, n):
            new_char = s2[i]
            window_count[ord(new_char)- ord('a')] += 1
            old_char = s2[i-k]
            window_count[ord(old_char)- ord('a')] -= 1

            if s1_count == window_count:
                return True
        return False
 
        
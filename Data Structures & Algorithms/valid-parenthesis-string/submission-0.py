class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin = 0
        lmax = 0
        for char in s:
            if char =="(":
                lmin += 1
                lmax += 1
            elif char ==")":
                lmin -= 1
                lmax -= 1
            else:
                lmin -= 1
                lmax += 1
            if lmax < 0:
                return False
            lmin = max(lmin, 0)
        return lmin == 0
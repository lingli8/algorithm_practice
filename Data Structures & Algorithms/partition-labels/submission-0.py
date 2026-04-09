class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index ={c: i for i, c in enumerate(s)}
        res = []
        start = 0
        end = 0
        for index, char in enumerate(s):
            end = max(end, last_index[char])
            if index == end:
                res.append(end - start + 1)
                start = index + 1
        return res

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        parts = [set() for _ in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num == '.':
                    continue
                part_index = (x//3) * 3+ y//3
                if (num in rows[x]) or (num in cols[y]) or (num in parts[part_index]):
                    return False
                rows[x].add(num)
                cols[y].add(num)
                parts[part_index].add(num)
        return True
            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        part = [set() for _ in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num == ".":
                    continue
                part_index = (x//3) *3 + (y//3)
                if (num in row[x]) or  (num in col[y]) or (num in part[part_index]):
                    return False

                row[x].add(num)
                col[y].add(num)
                part[part_index].add(num)
                
        return True
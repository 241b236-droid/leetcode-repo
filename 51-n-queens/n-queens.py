class Solution(object):
    def solveNQueens(self, n):
        result = []
        cols = set()
        diags = set()
        anti_diags = set()
        queens = [0] * n
        self._backtrack(0, n, queens, cols, diags, anti_diags, result)
        return result

    def _backtrack(self, row, n, queens, cols, diags, anti_diags, result):
        if row == n:
            # All queens placed successfully
            result.append(self._build_board(queens, n))
            return
        for col in range(n):
            diag = row - col
            anti_diag = row + col
            # Skip if column or diagonal is occupied
            if col in cols or diag in diags or anti_diag in anti_diags:
                continue
            # Place queen and mark occupied
            queens[row] = col
            cols.add(col)
            diags.add(diag)
            anti_diags.add(anti_diag)
            self._backtrack(row + 1, n, queens, cols, diags, anti_diags, result)
            # Remove queen and unmark (backtrack)
            cols.remove(col)
            diags.remove(diag)
            anti_diags.remove(anti_diag)

    def _build_board(self, queens, n):
        board = []
        for i in range(n):
            row = ['.'] * n
            row[queens[i]] = 'Q'
            board.append(''.join(row))
        return board
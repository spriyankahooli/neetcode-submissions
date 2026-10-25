class Solution:

  def solveNQueens(self, n: int) -> List[List[str]]:
    res = []
    # Keeps track of the column index for each row
    board = [-1] * n
    self.dfs(0, set(), set(), set(), n, board, res)
    return res

  def dfs(self, r, dia_set, ant_dia_set, col_set, n, board, res):
    if r == n:
      # Construct the visual board representation
      res.append(self.construct_board(board, n))
      return

    for c in range(n):
      curr_dia = r - c
      curr_ant = r + c

      if c in col_set or curr_dia in dia_set or curr_ant in ant_dia_set:
        continue

      col_set.add(c)
      ant_dia_set.add(curr_ant)
      dia_set.add(curr_dia)
      board[r] = c

      self.dfs(r + 1, dia_set, ant_dia_set, col_set, n, board, res)

      # Backtrack
      col_set.remove(c)
      ant_dia_set.remove(curr_ant)
      dia_set.remove(curr_dia)
      board[r] = -1

  def construct_board(self, board, n):
    visual_board = []
    for r in range(n):
      row_chars = ['.'] * n
      row_chars[board[r]] = 'Q'
      visual_board.append(''.join(row_chars))
    return visual_board
def print_sudoku(sudoku: list):
  row = 0
  while row < 9:
    column = 0
    while column < 9:
      if sudoku[row][column] == 0:
        if column > 0 and column % 3 == 0:
          print(" _ ", end="")
        else:
          print("_ ", end="")
      else:
        print(sudoku[row][column], end=" ")
      column += 1
    print()
    if row == 2 or row == 5:
      print()
    row += 1

        
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku[row_no][column_no] = number

# Sudoku Solver

This is a C++ program that solves Sudoku puzzles using a backtracking algorithm. Sudoku is a logic-based number placement game where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids (called "regions") contain all of the digits from 1 to 9 without repetition.

## How to Use

1. **Compile the Program:** Compile the C++ program using a C++ compiler (e.g., g++).

   ```bash
   g++ sudoku_solver.cpp -o sudoku_solver
   ```

2. **Run the Program:** Execute the compiled program.

   ```bash
   ./sudoku_solver
   ```

3. **Input Your Sudoku Puzzle:**
   - The program will prompt you to enter the Sudoku puzzle one row at a time.
   - Use the '.' character to represent empty cells in the puzzle.
   - Enter the digits of the puzzle row by row.

   Example input for a Sudoku puzzle:
   ```
   Enter Sudoku puzzle (use '.' for empty cells):
   53..7....
   6..195...
   .98....6.
   8...6...3
   4..8.3..1
   7...2...6
   .6....28.
   ...419..5
   ....8..79
   ```

4. **Solved Sudoku:**
   - The program will solve the Sudoku puzzle and display the solved grid.
   - If a solution exists, it will print the solved Sudoku.
   - If no solution exists for the provided input, it will indicate that no solution was found.

   Example output for a solved Sudoku:
   ```
   Solved Sudoku:
   5 3 4 6 7 8 9 1 2
   6 7 2 1 9 5 3 4 8
   1 9 8 3 4 2 5 6 7
   8 5 9 7 6 1 4 2 3
   4 2 6 8 5 3 7 9 1
   7 1 3 9 2 4 8 5 6
   9 6 1 5 3 7 2 8 4
   2 8 7 4 1 9 6 3 5
   3 4 5 2 8 6 1 7 9
   ```

## How the Program Works

- The program uses a backtracking algorithm to solve Sudoku puzzles.
- It starts by iterating through the empty cells of the puzzle.
- For each empty cell, it tries to fill it with values from 1 to 9 while ensuring that the value doesn't conflict with any other values in the same row, column, or 3x3 box.
- If a valid value is found, it proceeds recursively to solve the remaining puzzle.
- If no valid value is found, it backtracks to the previous cell and tries a different value.
- This process continues until the entire Sudoku puzzle is solved or determined to be unsolvable.

Feel free to use and modify this program to solve your own Sudoku puzzles or integrate it into other projects.

Enjoy solving Sudoku puzzles with this program!
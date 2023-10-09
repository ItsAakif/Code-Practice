#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // Function to check if it's safe to place 'value' at cell (row, col)
    bool isSafe(int row, int col, vector<vector<char>>& board, char value) {
        int n = board.size();

        for (int i = 0; i < n; i++) {
            // Row check
            if (board[row][i] == value)
                return false;

            // Column check
            if (board[i][col] == value)
                return false;

            // 3x3 box check
            if (board[3 * (row / 3) + (i / 3)][3 * (col / 3) + (i % 3)] == value)
                return false;
        }

        return true;
    }

    // Recursive function to solve the Sudoku puzzle
    bool solve(vector<vector<char>>& board) {
        int n = board.size();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check for an empty cell
                if (board[i][j] == '.') {
                    // Try to fill with values ranging from '1' to '9'
                    for (char val = '1'; val <= '9'; val++) {
                        // Check for safety
                        if (isSafe(i, j, board, val)) {
                            // Insert the value
                            board[i][j] = val;

                            // Recursively try to solve the remaining board
                            bool remainingBoardSolution = solve(board);
                            if (remainingBoardSolution == true) {
                                return true;
                            } else {
                                // Backtrack if no solution found
                                board[i][j] = '.';
                            }
                        }
                    }
                    // If no solution found from '1' to '9', backtrack
                    return false;
                }
            }
        }
        // All cells filled, puzzle solved
        return true;
    }

    // Function to solve the Sudoku puzzle
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
};

// Function to print the Sudoku board
void printSudoku(vector<vector<char>>& board) {
    int n = board.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to take Sudoku input from the user
void takeSudokuInput(vector<vector<char>>& board) {
    int n = board.size();
    cout << "Enter Sudoku puzzle (use '.' for empty cells):" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }
}

int main() {
    Solution sudokuSolver;
    vector<vector<char>> board(9, vector<char>(9, '.'));

    takeSudokuInput(board);

    sudokuSolver.solveSudoku(board);

    // Check if the puzzle was solved successfully
    cout << "Solved Sudoku:" << endl;
    printSudoku(board);

    return 0;
}

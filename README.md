# Sudoku
This script is able to solve just-above-medium difficulty Sudokus by implementing simple algorithms.

From this point on let's call the Sudoku.py file 'The App'.

I should first thank the people who made Numpy and Pandas available for public use, since this App has heavily used the objects in both modules.

## How to import your Sudoku
In the first stages of developing this app it could only communicate with the user through console window, but thanks to Pandas now it reads the input sudoko from the Sudoku.xlsx Excel file which is just next to the Python file. In order to input your sample sudoku look for the corresponding Excel Sheet Name (4x4, 9x9, 16x16) and use the highlighted area as your working cells. 
-A probable future version might try to look for ways to ease this process even further.

## How it works
Bear in mind that this app as of now can only solve sudokus using the simplest of methods and those are:
1. To check whether a number is the only possible choice for a cell by scanning and crossing out numbers that have been used in neighbouring cells in it's Row, Column and Block. 
2. To check if a number is the sole candidate for a cell by checking the possible choices for each neighboring cell in it's Row, Column and Block.
if so then we have a winner for that cell and we'll happily move to the next cell if not, we would still move along with solving cells following the current cell but remebering what were the remaining possible choices are for each cell.

## How the process ends
A limited number of iterations are done (i.e number of rows in power of 2), if the sudoku is solved before the iteration is over the completed soduko is returned, if the iteration exausts before solving the sudoku (typically happens if theres a loop going on) whatever of the sudoku that is solved is then returned.
-Another probable future version could address this issue by implementing more advanced methods or using the brute-force strategy.

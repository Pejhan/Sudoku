## Sudoku
This script is able to solve just-above-medium difficulty sudokus by implementing simple algorithms.

From this point on let's call the Sudoku.py file 'The App'.

I should first thank the people who made Numpy and Pandas available for public use, since this App has heavily used the objects in both modules.

# How to import your Sudoku
In the first stages of developing this app it could only communicate with the user through console window, but thanks to Pandas it reads the input sudoko from the Sudoku.xlsx Excel file that has been put just next to the Python file. In order to input your sample sudoku look for the corresponding Excel Sheet Name (4x4, 9x9, 16x16) and use the highlighted area as your working cells. 
-A probable future version might try to look for ways to ease this process.

# How it works
bear in mind that this app as of now can only solve sudokus using the simplest of methods and that is to check wether a number a unique in it's Row, Column or Block. if so then we have a winner for that cell and we'll happily move to the next cell if not, it would still move forward with solving cells following the current cell but remebering what are the remaining possible choices are for each cell.

# How the process ends
A limited number of iterations are done (i.e number of rows in power of 2), if the sudoku is solved before the iteration is over the completed soduko is returned, if the iteration exausts before solving the sudoku (typically happens if theres a loop going on) whatever of the sudoku that is solved is then returned.
-Another probable future version could address this issue by implementing more advanced methods or using the brute-force strategy.

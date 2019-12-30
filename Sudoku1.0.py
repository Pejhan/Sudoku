import numpy as np
import pandas as pd

d = 9
sd = int(d ** (1 / 2))

all_possible_choices = [i + 1 for i in range(d)]
rc = {}
raw_sudoku_df = pd.read_excel(io='sudoku.xlsx',
                              sheet_name=str(d) + "x" + str(d)
                              )


class Soduko:
    def __init__(self):
        self.s = np.array([0 for i in range(d ** 2)]).reshape(d, sd, sd)
        self.x = []
        self.y = []
        self.z = []

    def imprt(self, rsd):
        for br in range(sd):
            for bc in range(sd):
                self.s[br * sd + bc] = np.array(rsd.iloc[br * sd: br * sd + sd,
                                                        bc * sd: bc * sd + sd]
                                                              )
        for i in range(0, d):
            self.x.append(list(np.array(rsd.iloc[i, :])))
            self.y.append(list(np.array(rsd.iloc[:, i])))
            self.z.append(list(np.hstack(self.s[i])))

    def copy(self, s):
        self.s = s.s[:]
        self.x = s.x[:]
        self.y = s.y[:]
        self.z = s.z[:]

sudoku = Soduko()
sudoku.imprt(raw_sudoku_df)


def disp_sudoku(s):
    ###Used to display "sudoku" in the process if anywhere needed
    for br in range(sd):
        for r in range(sd):
            for bc in range(sd):
                for c in range(sd):
                    if (bc + 1) % sd == 0 and c + 1 == sd :
                        print(s.s[(br * sd) + bc][r][c])
                    elif c + 1 == sd:
                        print(s.s[(br * sd) + bc][r][c], end="\t|\t")
                    else:
                        print(s.s[(br * sd) + bc][r][c], end="\t\t")
                    if (bc + 1) % sd == 0 and c + 1 == sd and r + 1 == sd:
                        print('')
    print('-------------------------------------------------------------------------')

def qrc(s):
    ###Creating a dictionary for each unsolved cell and then filling them with respective available choices and taking care of the unneccessary ones
    for i in range(d):
        for j in range(d):
            if s.x[i][j] == 0:
                if (i, j) not in rc.keys():
                    rc[(i, j)] = all_possible_choices[:]

                for k in all_possible_choices:
                    if k in rc[(i, j)]:
                        if k in s.x[i] or k in s.y[j] or k in s.z[(i // sd) * sd + (j // sd)]:
                            rc[(i, j)].remove(k)

    ###Remaining choices cleanup
    _tmp_rc = rc.copy()
    for k, v in _tmp_rc.items():
        if v == []:
            del rc[k]


def solve(s):
    ###Checks what cells requires "handl"ing and sends the corresponding command
    for br in range(sd):
        for bc in range(sd):
            for r in range(sd):
                for c in range(sd):
                    if s.s[br * sd + bc][r][c] == 0:
                        handle(s, br, bc, r, c)

def assignValue(s, br, bc, r, c, v):
    ###Assigns the proposed value in sudoku and all of its derivitives and takes care of the remaining_choices variable
    s.s[br * sd + bc][r][c] = v
    s.x[br * sd + r][bc * sd + c] = v
    s.y[bc * sd + c][br * sd + r] = v
    s.z[br * sd + bc][r * sd + c] = v
    del rc[(br * sd + r, bc * sd + c)]

def singleCandidate(s, br, bc, r, c):
    qrc(s)
    if (br * sd + r, bc * sd + c) in rc.keys():
        if len(rc[(br * sd + r, bc * sd + c)]) == 1:
            assignValue(s, br, bc, r, c, rc[(br * sd + r, bc * sd + c)][0])
    # else:
    #     rc[(br * sub_dim + r, bc * sub_dim + c)] = possible_choices_for_the_current_cell

def onlyPossibleCell(s, br, bc, r, c):
    # print(list(rc.keys()).count((br * sub_dim + r, bc * sub_dim + c)))
    qrc(s)
    if list(rc.keys()).count((br * sd + r, bc * sd + c)) != 0:
        if len(rc[(br * sd + r, bc * sd + c)]) != 0:
            while True:
                a = set(rc[(br * sd + r, bc * sd + c)])
                ## Only Possible Cell in the block
                for i in range(sd):
                    for j in range(sd):
                        if (i, j) != (r, c):
                            if list(rc.keys()).count((br * sd + i, bc * sd + j)) != 0:
                                if len(rc[(br * sd + i, bc * sd + j)]) != 0:
                                    b = set(rc[(br * sd + i, bc * sd + j)])
                                    a = set(a).difference(b)
                if len(a) == 1:
                    break

                # Only Possible Cell in the row
                for j in range(d):
                    if j != bc * sd + c:
                        if list(rc.keys()).count((br * sd + r, j)) != 0:
                            if len(rc[(br * sd + r, j)]) != 0:
                                b = set(rc[(br * sd + r, j)])
                                a = set(a).difference(b)
                if len(a) == 1:
                    break

                # Only Possible Cell in the col
                for i in range(d):
                    if i != br * sd + r:
                        if list(rc.keys()).count((i, bc * sd + c)) != 0:
                            if len(rc[(i, bc * sd + c)]) != 0:
                                b = set(rc[(i, bc * sd + c)])
                                a = set(a).difference(b)
                if len(a) == 1:
                    break

                break

            if len(a) == 1:
                assignValue(s, br, bc, r, c, list(a)[0])


def handle(s, br, bc, r, c):
    ###"Handle"s the given cell
    singleCandidate(s, br, bc, r, c)
    onlyPossibleCell(s, br, bc, r, c)


for i in range(1, d * 2):
    flat_sudoku = np.hstack(np.hstack(sudoku.s))
    if 0 in flat_sudoku:
        solve(sudoku)
    else:
        break

disp_sudoku(sudoku)

# print(rc)
# print(len(rc))

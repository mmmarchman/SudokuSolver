__author__ = 'McClain Marchman'

import sys


loop_counter = 0


class SudokuSolver:

    def __init__(self):

        self.parse_file("EasyPuzzle157.txt")

    # Looks for 0 indexes with only one possibility and then changes that index
    # Each for loop represents a square since I could not come up with a loop that parsed the way I wanted to
    def solve(self, rows, columns, squares):

        # Square: 0 Rows: 0-2 Columns: 0-2
        for c in range(0, 3):
            for r in range(0, 3):
                possible_values = self.possible_values(rows[r], columns[c], squares[0])
                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 1 Rows: 3-5 Columns: 0-2
        for c in range(0, 3):
            for r in range(3, 6):
                possible_values = self.possible_values(rows[r], columns[c], squares[1])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 2 Rows: 6-8 Columns: 0-2
        for c in range(0, 3):
            for r in range(6, 9):
                possible_values = self.possible_values(rows[r], columns[c], squares[2])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 3 Rows: 0-2 Columns: 3-5
        for c in range(3, 6):
            for r in range(0, 3):
                possible_values = self.possible_values(rows[r], columns[c], squares[3])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 4 Rows: 3-5 Columns: 3-5
        for c in range(3, 6):
            for r in range(3, 6):
                possible_values = self.possible_values(rows[r], columns[c], squares[4])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 5 Rows: 6-8 Columns: 3-5
        for c in range(3, 6):
            for r in range(6, 9):
                possible_values = self.possible_values(rows[r], columns[c], squares[5])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 6 Rows: 0-2 Columns: 6-8
        for c in range(6, 9):
            for r in range(0, 3):
                possible_values = self.possible_values(rows[r], columns[c], squares[6])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 7 Rows: 3-5 Columns: 6-8
        for c in range(6, 9):
            for r in range(3, 6):
                possible_values = self.possible_values(rows[r], columns[c], squares[7])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        # Square: 8 Rows: 6-8 Columns: 6-8
        for c in range(6, 9):
            for r in range(6, 9):
                possible_values = self.possible_values(rows[r], columns[c], squares[8])

                if len(possible_values) <= 1:
                    rows = self.change_value(rows, r, c, possible_values)

        return rows

    def change_value(self, rows_c, row_index, column_index, possible_values):

        global loop_counter
        #Sleep so we can see the progress
        #time.sleep(.2)

        # Check to see if we are finished
        index = 0
        for f in range(0, 9):
            if '0' not in rows_c[f] and index >= len(rows_c)-1:
                print "!!!!!FINISHED!!!!!!!"
                self.write_rcs(rows_c)
                sys.exit(0)
            elif '0' not in rows_c[f]:
                index += 1

        # Print current status of the solve to the outputfile
        self.write_rcs(rows_c)

        x = list(rows_c[row_index])

        if x[column_index] == str(0):
            x[column_index] = str(possible_values)
            loop_counter += 1
            x = ''.join(x)
            x = x.replace('[', '')
            x = x.replace(']', '')
            del rows_c[row_index]
            rows_c.insert(row_index, x)
            print "Loop Counter: "
            print loop_counter

        #else:

            #print "Cannot remove! Not a zero!"

        return rows_c

    def create_column_squares(self, rows):

        columns = []
        squares = []

        # Parse row data into column data and remove commas
        for i in range(0, 9):
            columns.append([row[i] for row in rows])
            columns[i] = ''.join(columns[i])

        # Take the first three entries from rows[] and append it to squares[]
        for i in range(0, 9):
            squares.append(rows[i][:3])

        # Take the middle three entries from rows[] and append it to squares[]
        for i in range(0, 9):
            squares.append(rows[i][3:6])

        # Take the last three entries from rows[] and append it to squares[]
        for i in range(0, 9):
            squares.append(rows[i][6:9])

        # Combine the sets of three to form a list containing the elements for the 3X3 matrix
        squares[0] = squares[0] + squares[1] + squares[2]
        squares[1] = squares[3] + squares[4] + squares[5]
        squares[2] = squares[6] + squares[7] + squares[8]

        squares[3] = squares[9] + squares[10] + squares[11]
        squares[4] = squares[12] + squares[13] + squares[14]
        squares[5] = squares[15] + squares[16] + squares[17]

        squares[6] = squares[18] + squares[19] + squares[20]
        squares[7] = squares[21] + squares[22] + squares[23]
        squares[8] = squares[24] + squares[25] + squares[26]

        # Delete the unused sets of three from squares[]
        del squares[len(squares)-18:]

        return columns, squares

    # Find the possible values of a row, column, or square
    def possible_values(self, row, column, square):

        all_possible_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        all_possible_column = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        all_possible_square = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for r in range(1, 10):
            if str(r) in row:
                try:
                    all_possible_row.remove(r)
                except Exception, e:
                    print e
                    continue
            if str(r) in column:
                try:
                    all_possible_column.remove(r)
                except Exception, e:
                    print e
                    continue
            if str(r) in square:
                try:
                    all_possible_square.remove(r)
                except Exception, e:
                    print e
                    continue

        all_possible_output = list(set(all_possible_row) & set(all_possible_column) & set(all_possible_square))

        #print "All possible output: " + str(all_possible_output)

        return all_possible_output

    def write_rcs(self, rows):

        with open("outputSolvedSudoku.sudoku", 'w+') as out_file:
            for row in rows:
                row = ''.join(row)
                print row
                out_file.write(row+'\n')
            print '-------------------------------------------------------'


    def parse_file(self, file_name):
        """Takes in a .txt file as input where each integer,separated by a comma, represents a location on a Sudoku board.
        A zero indicates an empty space on the board."""

        with open(file_name) as input_file:
            rows = input_file.readlines()

        # Removes newline characters in rows
        rows = map(lambda s: s.strip(), rows)

        # Removes commas from the row list
        rows = [r.replace(',', '') for r in rows]

        while rows.count(0) is 0:
            columns, squares = self.create_column_squares(rows)
            rows = self.solve(rows, columns, squares)


if __name__ == '__main__':
    solver = SudokuSolver()


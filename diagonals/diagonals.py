board_lines = ['-', '/', '\\', ' ']


def main():
    N = 16
    w = 5
    b = Board(w)

    fill_board(b, N)


def fill_board(b, N):
    """Fill board (b) up to (N) lines and find all possible solutions
    using backtracking
    """
    if b.get_lines() == N:
        return N
    if b.size() < N:
        return False
    row = (0, 0)
    lines = [-1, 0, 1, 2]
    line = lines[b.get_row_value(row)]
    s = 0
    while True:
        if b.is_valid_line(row, line):
            if b.set_row(row, line) == N:
                print('##### Solution! #####')
                print(b, 'N =', b.get_lines(), '\n')
                s = 1
            if (b.remaining_rows(row) + b.get_lines()) < N or s == 1:
                # Reached end of board or useless branch, need to backtrack
                s = 0
                b.set_row(row, -1)  # reset current row
                row = b.previous_row(row)
                line = lines[b.get_row_value(row)]
            else:
                row = b.next_row(row)
                line = lines[b.get_row_value(row)]
        else:
            line -= 1
        while line < 0:
            # Need to backtrack
            b.set_row(row, -1)  # reset current row
            if row != (0, 0):
                row = b.previous_row(row)
                line = lines[b.get_row_value(row)]
            else:
                return False
    return N


class Board(object):
    """ A square board object

    """
    def __init__(self, width):
        self.__width = width      # board width
        self.__height = width     # board height
        self.__board = dict()     # each entry represents a row in the board
        self.__lines = 0          # how many lines are on the board
        for i in range(self.__width):
            for j in range(self.__height):
                self.__board[(i, j)] = -1

    def dimensions(self):
        """Returns boards dimensions as a tuple (width, height)
        """
        return (self.__width, self.__height)

    def size(self):
        """Returns board size width x height
        """
        return self.__width * self.__height

    def set_row(self, row, line):
        """Sets the value of a row

        Inputs:
            row: a tuple (x, y) coordinates
            line: an int it could be one of the following values
                values: 0 - empty row
                        1 - line with positive slope
                        2 - line with negative slope
                        -1 - not set

        Return:
            Number of lines on the board, -1 on error
        """
        if line not in [-1, 0, 1, 2]:
            return -1

        if row not in self.__board:
            return -1

        # change row value and update line counter
        if self.__board[row] > 0:
            self.__lines -= 1
        self.__board[row] = line
        if line > 0:
            self.__lines += 1
        return self.__lines

    def get_row_value(self, row):
        """Returns the value on the given row, -1 if row not on board
        """
        if row not in self.__board:
            return -1
        return self.__board[row]

    def get_lines(self):
        """Returns number of lines currently on the board
        """
        return self.__lines

    def next_row(self, row):
        """Returns the next row of the Board
        The Board starts at coordinates (0, 0) from the bottom left
        and ends in coordinates (width-1, height-1) in the upper right

        Inputs:
            row: a tuple (x, y)

        Returns:
        next_row: a tuple (x, y) on success / (-1, -1) if the current row
        is the last row of the board
        """
        # if row not in board return (-1, -1)
        if row not in self.__board:
            return (-1, -1)
        # if current row is the last row return (-1, -1)
        if row == (self.__width - 1, self.__height - 1):
            return (-1, -1)

        if row[0] == self.__width - 1:
            return (0, row[1] + 1)
        return (row[0] + 1, row[1])

    def previous_row(self, row):
        """Returns the previous row of the Board
        The Board starts at coordinates (0, 0) from the bottom left
        and ends in coordinates (width-1, height-1) in the upper right

        Inputs:
            row: a tuple (x, y)

        Returns:
            next_row: a tuple (x, y) on success / (-1, -1) if the current row
            is the first row of the board
        """
        # if row not in board return (-1, -1)
        if row not in self.__board:
            return (-1, -1)
        # if current row is the first row return (-1, -1)
        if row == (0, 0):
            return (-1, -1)

        if row[0] == 0:
            return (self.__width - 1, row[1] - 1)
        return (row[0] - 1, row[1])

    def is_valid_line(self, row, line):
        """Returns True if the line doesn't touch any other adjacent line
        """
        x, y = row
        if line < 1:
            return True

        if line == 1:
            # must check for indexes (x-1, y), (x-1, y-1), (x, y-1)
            # (x-1, y) can't be 1
            if self.get_row_value((x-1, y)) == 2:
                return False
            # (x-1, y-1) can't be 2
            if self.get_row_value((x-1, y-1)) == 1:
                return False
            # (x, y-1) can't be 1
            if self.get_row_value((x, y-1)) == 2:
                return False
            return True

        if line == 2:
            # must check for indexes (x-1, y), (x, y-1), (x+1, y-1)
            # (x-1, y) can't be 2
            if self.get_row_value((x-1, y)) == 1:
                return False
            # (x+1, y-1) can't be 1
            if self.get_row_value((x+1, y-1)) == 2:
                return False
            # (x, y-1) can't be 2
            if self.get_row_value((x, y-1)) == 1:
                return False
            return True

        return False

    def remaining_rows(self, row):
        """return amount of remaining rows end - row
        """
        return self.size() - (row[0] + 1) - (row[1]) * self.__height

    def __str__(self):
        board = '\n'
        for j in range(self.__height - 1, -1, -1):
            row = ''
            for i in range(self.__width):
                row += ' | ' + board_lines[(self.__board[(i, j)])]
            board += row + ' | ' + '\n'
        return board


if __name__ == '__main__':
    main()

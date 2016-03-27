def check(l):
    """
        If the sum of all the items in the list is twelve, then it returns True, if not, False
        :argument l: The list that is checked
        :returns True/False: Whether it sums to twelve or not
        """
    if sum(l) == 12:
        return True
    else:
        return False


class Grid:
    def __init__(self, x, fill):
        """
        Creates a grid with the number of squares on the x axis and number of squares on the y axis given
        :argument x: The number of squares on the x axis
        :argument fill: The thing to fill each square with
        :returns grid: The final empty grid
        """
        self.grid = []
        for j in range(0, x):
            self.grid.append([])
            for k in range(0, len(self.grid)):
                self.grid[k].append(fill)
        self.rows = []
        row = []
        for x in self.grid:
            for y in x:
                row.append(y)
            self.rows.append(row)
            row = []
        self.columns = []
        column = []
        for x in range(0,len(self.grid[0])):
            for y in range(0,len(self.grid)):
                column.append(self.grid[y][x])
            self.columns.append(column)
            column = []
        self.diagonals = [[],[]]
        for x in range(0,len(self.grid)):
            for y in range(0,len(self.grid[x])):
                if x == y:
                    self.diagonals[0].append(self.grid[x][y])
                if x == (len(self.grid[0])-1)-y:
                    self.diagonals[1].append(self.grid[x][y])

    def checkgrid(self):



    def fill(self, grid):

        #while check(grid[])
            for x in grid:
                for y in x:
                    print(y)

#grid = creategrid(4, 4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
g1 = Grid(5, '')
#fill(grid)
for i in g1.grid:
    print(i)
g1.checkgrid()
del g1
"""
GRID = [


        ]
"""
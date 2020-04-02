class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0

        total_island = 0

        # create a map to indicate exploratory path
        explored_map = []
        for _ in xrange(height):
            row = []
            for _ in xrange(width):
                row.append(False)
            explored_map.append(row)

        for row in xrange(height):
            for column in xrange(width):
                # This field has been checked. Skip it.
                if explored_map[row][column] is True:
                    continue
                # If this field is water, mark as checked then skip.
                elif grid[row][column] == '0':
                    explored_map[row][column] = True
                    continue
                # If this field is land and hasn't been checked.
                else:
                    total_island += 1
                    # Explore neighbor
                    stack = [(row, column)]
                    while len(stack) != 0:
                        pole = stack.pop()
                        # If this point is examined before, skip.
                        if explored_map[pole[0]][pole[1]] is True:
                            continue

                        explored_map[pole[0]][pole[1]] = True

                        # check possible neighbor
                        # check top side
                        if pole[0] != 0:
                            target_row = pole[0] - 1
                            target_column = pole[1]
                            # if not checked before
                            if explored_map[target_row][target_column] is not True:
                                # if neighbor is land
                                if grid[target_row][target_column] != '0':
                                    stack.append((target_row, target_column))
                        # check down side
                        if pole[0] != height - 1:
                            target_row = pole[0] + 1
                            target_column = pole[1]
                            if explored_map[target_row][target_column] is not True:
                                if grid[target_row][target_column] != '0':
                                    stack.append((target_row, target_column))
                        # check left side
                        if pole[1] != 0:
                            target_row = pole[0]
                            target_column = pole[1] - 1
                            if explored_map[target_row][target_column] is not True:
                                if grid[target_row][target_column] != '0':
                                    stack.append((target_row, target_column))
                        # check right side
                        if pole[1] != width - 1:
                            target_row = pole[0]
                            target_column = pole[1] + 1
                            if explored_map[target_row][target_column] is not True:
                                if grid[target_row][target_column] != '0':
                                    stack.append((target_row, target_column))

        return total_island


if __name__ == "__main__":
    runner = Solution()
    map = """\
11000
11000
00100
00011
"""
    input_data = []
    for line in map.split():
        one_list = []
        for char in line:
            one_list.append(char)
        input_data.append(one_list)

    return_data = runner.numIslands(input_data)
    print(return_data)

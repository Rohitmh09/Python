nums = [[0, 3, 3, 0], [6, 6, 1, 4], [3, 2, 5, 3], [7, 8, 6, 5]]
arr = []
for row in range(len(nums)):
    for item in range(len(nums[row])):
        print(nums[row][item], end=" ")
        if nums[row][item] == 0:
            arr.append([row, item])
    print()

print(arr)

# access it
for val in arr:
    print(val[0], val[1])

for val in arr:
    for row in range(len(nums)):
        for item in range(len(nums[row])):
            if val[0] == row or val[1] == item:
                nums[row][item] = 0

for row in range(len(nums)):
    for item in range(len(nums[row])):
        print(nums[row][item], end=" ")

    print()


# Optimal solution
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_t = set()
        col_t = set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    row_t.add(row)
                    col_t.add(col)

        for row in range(m):
            for col in range(n):
                if row in row_t or col in col_t:
                    matrix[row][col] = 0

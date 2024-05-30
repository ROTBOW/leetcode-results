class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        # Apply rows and cols to matrix
        # loop over r for row
        #   check if r is in rows(set)
        #       if so, turn the entire row to zero then continue the loop
        #   loop over c for col
        #       if any c is in cols(set)
        #           turn that position to zero

        for r in range(len(matrix)):
            if r in rows: # this whole row needs to be zeros
                matrix[r] = [0] * len(matrix[r])
                continue

            for c in range(len(matrix[r])):
                if c in cols:
                    matrix[r][c] = 0
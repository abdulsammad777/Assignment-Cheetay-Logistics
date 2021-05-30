def spirallyTraverse(R, C, matrix):
    row_min, row_max = 0, R-1
    col_min, col_max = 0, C-1
    n = R * C
    counter = 0
    Spiral_form = []
    while counter < n:
        j, k = row_min, col_min
        while k <= col_max:
            Spiral_form.append(matrix[j][k])
            k += 1
            counter += 1
        row_min += 1
        if counter == n:
            break

        j, k = row_min, col_max

        while j <= row_max:
            Spiral_form.append(matrix[j][k])
            j += 1
            counter += 1
        col_max -= 1

        if counter == n:
            break

        j, k = row_max, col_max

        counter += 1
        while k >= col_min:
            Spiral_form.append(matrix[j][k])
            k -= 1
            counter += 1
        row_max -= 1

        if counter == n:
            break
        j, k = row_max, col_min

        while j >= row_min:
            Spiral_form.append(matrix[j][k])
            j -= 1
            counter +=1
        col_min += 1

        if counter == n:
            break
    return Spiral_form

matrix = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15,16]]

print(spirallyTraverse(4, 4, matrix))


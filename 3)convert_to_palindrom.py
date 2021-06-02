
def countMin(s):
    if len(s) == 1:
        return 0
    # reversing string and checking for pre condition.
    reverse = ''
    for i in range(len(s)-1, -1, -1):
        reverse += (s[i])
    if s == reverse:
        return 0
    len_ = len(s)
    a,b = s,reverse
    matrix = []
    for i in range(len_+1):
        row = []
        for j in range(len_+1):
            row.append(0)
        matrix.append(row)


    for i in range(1,len_+1):
        for j in range(1,len_+1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return len_ - matrix[-1][-1]

print(countMin('abcd'))




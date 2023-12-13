import sys


def fill_mtx(rows, columns) :
    mtx = [[column for column in range(columns)] for row in range(rows)]
    i = 0
    while i < rows :
        j = 0
        while j < columns :
            print("Insert the element in position (", i, ",", j, "):")
            v = float(input())
            mtx[i][j] = v
            j += 1
        i += 1
    return (mtx)


def mtx_sum(mtx, rows, columns) :
    sums_rows = []
    sums_colums = []
    sum_r = 0
    sum_c = 0
    for i in range(rows) :
        for j in range(columns) :
            #print(i, j, mtx[i][j])
            sum_r += mtx[i][j]
        sums_rows.append(sum_r)
        sums_colums.append(sum_c)
        sum_r = 0
        sum_c = 0
    print("sum-> ", sum_r, "sumSr-> ", sums_rows)
    print("sum-> ", sum_c, "sumSc-> ", sums_colums)


if (len(sys.argv) != 3) :
    print("Error! Usage: python3 ft_matrix.py <n> <m>")
else :
    mtx = fill_mtx(int(sys.argv[1]), int(sys.argv[2]))
    print("matrix-> ", mtx)
    mtx_sum(mtx, int(sys.argv[1]), int(sys.argv[2]))


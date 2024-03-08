import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

def check(i,j,elems,n):
    count = 0

    if i - 1 != -1 and j - 1 != -1 and elems[i - 1][j - 1]== "#":
        count = count + 1
    if i - 1 != -1 and elems[i - 1][j]== "#":
        count = count + 1
    if i - 1 != -1 and j + 1 != n and elems[i - 1][j + 1]== "#":
        count = count + 1

    if j - 1 != -1 and elems[i][j - 1]== "#":
        count = count + 1
    if j + 1 != n and elems[i][j + 1]== "#":
        count = count + 1

    if i + 1 != n and j - 1 != -1 and elems[i + 1][j - 1]== "#":
        count = count + 1
    if i + 1 != n and elems[i + 1][j]== "#":
        count = count + 1
    if i + 1 != n and j + 1 != n and elems[i + 1][j + 1]== "#":
        count = count + 1

    return count.__str__()

if __name__ == "__main__":
    n = int(input().strip())
    element_matrix = []
    for i in range(0,n):
        element_row = [element for element in input().split("   ")]
        element_matrix.append(element_row)

    result = []
    for i in range(0,n):
        result_row = []
        for j in range(0,n):
            if element_matrix[i][j] == "-":
                result_row.append(check(i,j,element_matrix,n))
            else:
                result_row.append("#")
        result.append(result_row)


    for row in result:
        txt = "   ".join(row)
        print(txt)
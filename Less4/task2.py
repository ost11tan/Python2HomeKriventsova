"""✔Напишите функцию для транспонирования матрицы"""


def matrix(start_matrix:list[list[int]]) -> list[list[int]]:
    new_matrix=[]
    for row in range(len(start_matrix[0])):
        new_matrix.append(list())
        for elem in range(len(start_matrix)):
            new_matrix[row].append(start_matrix[elem][row])
    return new_matrix


def PRINT(mass:list[list[int]])->None:
    for row in mass:
        for elem in row:
            print(elem, end=' ')
        print()



if __name__=='__main__':
    st_matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Исходная матрица:")
    PRINT(st_matrix)
    print("Результирующая матрица:")
    PRINT(matrix(st_matrix))

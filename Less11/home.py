"""Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения,
 *умножения матриц"""


class Matrix:
    """Coздание класса Матрицы"""

    def __init__(self, mat: list[list], id: str = None):
        self.matrix = mat
        if id == None:
            id = "id"
        self.id = str(id)

    # def __str__(self):
    #   for row in self.matrix:
    #       for elem in row:
    #           print(elem, end=' ')
    #       print()
    #   return f"матрица {self.id}"

    def __repr__(self):
        for row in self.matrix:
            for elem in row:
                print(elem, end='\t')
            print()
        return f"матрица {self.id}"

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if not (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
            return f"Матрицы нельзя сложить!"
        else:
            return Matrix(
                [[self.matrix[row][elem] + other.matrix[row][elem] for elem in range(len(self.matrix[0]))] for row in
                 range(len(self.matrix))], self.id + "+" + other.id)

    def __mul__(self, other):
        if not (len(self.matrix[0]) == len(other.matrix)):
            return f"Матрицы нельзя перемножить!"
        else:
            k = len(other.matrix[0])
            result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for row in range(len(self.matrix)):
                for elem in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        result[row][elem] += self.matrix[row][k] * other.matrix[k][elem]
        return Matrix(result, self.id + "*" + other.id)


if __name__ == "__main__":
    matrix1 = Matrix([[1, 2, 3, 5], [4, 5, 6, 5], [7, 8, 9, 6]], 1)
    matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]], 3)
    # matrix2 = Matrix([[9, 8, 7], [6, 5, 2], [3, 2, 1]], 2)
    print(Matrix.__doc__)
    print(repr(matrix1))
    print(repr(matrix2))
    print(f"Матицы равны {matrix2 == matrix1}")
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)

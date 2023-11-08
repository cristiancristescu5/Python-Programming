import numpy as np


class Matrix:
    def __init__(self, rows, cols, matrix = None):
        if matrix is None:
            self.rows = rows
            self.cols = cols
            self.matrix = np.zeros((rows, cols))
        else:
            self.cols = matrix[0].size
            self.rows = matrix.size / self.cols
            self.matrix = matrix

    def set(self, i, j, data):
        if (i < 0 or i >= self.rows) and (j < 0 or j >= self.cols):
            print("Index out of range")
            return
        self.matrix[i, j] = data

    def get(self, i, j):
        if (i < 0 or i >= self.rows) and (j < 0 or j >= self.cols):
            print("Index out of range")
            return
        return self.matrix[i, j]

    def transpose(self):
        new_matrix = np.transpose(self.matrix)
        self.matrix = new_matrix
        temp = self.rows
        self.rows = self.cols
        self.cols = temp

    def multiply(self, mat):
        if self.cols != mat.rows:
            print("Invalid matrix")
            return

        result = np.dot(self.matrix, mat.matrix)
        return Matrix(self.rows, mat.cols, matrix=result)

    def apply(self, func):
        self.matrix = np.vectorize(func)(self.matrix)

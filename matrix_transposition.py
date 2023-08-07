def transpose_matrix(matrix: list) -> list:
    return list(map(list, zip(*matrix)))


user_matrix = [[1, 2, 3, 7], [4, 5, 6, 9]]
print(transpose_matrix(user_matrix))

def matrix_to_dict(matrix:list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i: k for i, k in enumerate(matrix, 1)}

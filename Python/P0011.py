from functools import reduce
from operator import mul


def load_matrix(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        return [[int(col) for col in row.split(" ")] for row in f]


def check_products(matrix: list[list[int]], coordinate: tuple[int, int]) -> int:
    row_prod = reduce(mul, (matrix[coordinate[0]][coordinate[1] + i] for i in range(4)))
    col_prod = reduce(mul, (matrix[coordinate[0] + i][coordinate[1]] for i in range(4)))
    diag_down_prod = reduce(mul, (matrix[coordinate[0] + i][coordinate[1] + i] for i in range(4)))
    diag_up_prod = reduce(mul, (list(reversed(matrix))[coordinate[0] + i][coordinate[1] + i] for i in range(4)))
    return max(row_prod, col_prod, diag_down_prod, diag_up_prod)


def find_max(matrix: list[list[int]]) -> int:
    return max(check_products(matrix, (row, col)) for row in range(len(matrix) - 3) for col in range(len(matrix[row]) - 3))


def main() -> None:
    matrix = load_matrix("../Input/P0011.txt")
    answer = find_max(matrix)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

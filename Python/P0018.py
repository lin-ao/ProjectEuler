def load_input(file_path: str) -> list[list[int]]:
    with open(file_path, "r") as f:
        pyramid = [[int(number) for number in line.rstrip("\n").split(" ")] for line in f]
        return pyramid


def reduce_row(pyramid: list[list[int]]) -> list[list[int]]:
    for i in range(len(pyramid[-2])):
        pyramid[-2][i] += max(pyramid[-1][i], pyramid[-1][i + 1])
    return pyramid[:-1]


def calculate_path(pyramid: list[list[int]]) -> int:
    while len(pyramid) > 1:
        pyramid = reduce_row(pyramid)
    return pyramid[0][0]


def main() -> None:
    test_input = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    assert calculate_path(test_input) == 23
    pyramid = load_input("../Input/P0018.txt")
    answer = calculate_path(pyramid)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

from functools import reduce
from operator import mul


def load_input(path: str) -> int:
    with open(path, "r") as f:
        return int(*f)


def int_to_list(number: int) -> list[int]:
    return list(map(int, list(str(number))))


def find_max_product(number: int, window: int) -> int:
    digits = int_to_list(number)
    return max(reduce(mul, digits[i:(i + window)]) for i in range(len(digits) - window))


def main() -> None:
    number = load_input("../Input/P0008.txt")
    assert find_max_product(number, 4) == 5832
    answer = find_max_product(number, 13)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

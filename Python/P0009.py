from functools import reduce
from operator import mul


def check_pythagoras(a: int, b: int, c:int) -> bool:
    return a ** 2 + b ** 2 == c ** 2


def find_triplets(total: int) -> tuple[int, int, int]:
    for a in range(total, 0, -1):
        for b in range(total - a, 0, -1):
            c = total - a - b
            if check_pythagoras(a, b, c):
                return a, b, c


def main() -> None:
    answer = reduce(mul, find_triplets(1000))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

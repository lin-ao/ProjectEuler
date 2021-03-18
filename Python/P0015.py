from math import factorial


# Permutations of multiset
def calculate_paths(side: int) -> int:
    return factorial(side * 2) // (factorial(side) * factorial(side))


def main() -> None:
    assert calculate_paths(2) == 6
    answer = calculate_paths(20)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

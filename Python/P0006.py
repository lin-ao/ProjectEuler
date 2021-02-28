def sum_of_squares(upper: int) -> int:
    return sum(map(lambda x: x ** 2, range(upper + 1)))


def square_of_sum(upper: int) -> int:
    return sum(range(upper + 1)) ** 2


def calculate_answer(upper: int) -> int:
    return square_of_sum(upper) - sum_of_squares(upper)


def main() -> None:
    assert calculate_answer(10) == 2640
    answer = calculate_answer(100)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()

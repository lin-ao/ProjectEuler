from math import factorial


def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(number))


def main() -> None:
    assert digit_sum(factorial(10)) == 27
    answer = digit_sum(factorial(100))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

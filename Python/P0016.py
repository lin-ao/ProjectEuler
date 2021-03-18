def sum_digits(number: int) -> int:
    return sum(int(digit) for digit in list(str(number)))


def main() -> None:
    assert sum_digits(2 ** 15) == 26
    answer = sum_digits(2 ** 1000)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

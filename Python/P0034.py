from math import factorial


def calculate_factorials(number: int) -> int:
    return sum(factorial(int(num)) for num in list(str(number)))


def calculate_sum(threshold: int) -> int:
    return sum((number) for number in range(10, threshold) if calculate_factorials(number) == number)


def main() -> None:
    assert calculate_factorials(145) == 145
    answer = calculate_sum(50000)
    print(answer)


if __name__ == "__main__":
    main()

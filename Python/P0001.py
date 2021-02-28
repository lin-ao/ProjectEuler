def check_multiples(number: int) -> bool:
    return number % 3 == 0 or number % 5 == 0


def sum_multiples(upper: int) -> int:
    return sum(filter(check_multiples, range(upper)))


def main() -> None:
    assert sum_multiples(10) == 23
    answer = sum_multiples(1000)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()

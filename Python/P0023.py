from itertools import product
from math import sqrt


def sum_of_divisors(number: int) -> int:
    return sum(sum({num, number // num}) for num in range(2, int(sqrt(number)) + 1) if number % num == 0) + 1


def is_abundant(number: int) -> bool:
    return sum_of_divisors(number) > number


def find_abundant_numbers(upper: int) -> list[int]:
    return [number for number in range(1, upper + 1) if is_abundant(number)]


def sums_of_abundant_numbers(upper: int) -> list[int]:
    return set(filter(lambda x: x <= upper, [sum(pair) for pair in product(find_abundant_numbers(upper), repeat=2)]))


def sum_of_non_abundant_sums(upper: int) -> int:
    soan = sums_of_abundant_numbers(upper)
    return sum(number for number in range(upper + 1) if not number in soan)


def main() -> None:
    answer = sum_of_non_abundant_sums(28123)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

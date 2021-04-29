from math import sqrt


def sum_of_divisors(number: int) -> int:
    return sum(sum({num, number // num}) for num in range(2, int(sqrt(number)) + 1) if number % num == 0) + 1


def find_amicable_numbers(upper: int) -> list[int]:
    amicable_numbers = set()
    for number in range(1, upper + 1):
        divisor_sum = sum_of_divisors(number)
        if divisor_sum != number and sum_of_divisors(divisor_sum) == number:
            amicable_numbers.update({number, divisor_sum})
    return amicable_numbers


def main() -> None:
    assert sum_of_divisors(220) == 284
    assert sum_of_divisors(284) == 220
    answer = sum(find_amicable_numbers(10000))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

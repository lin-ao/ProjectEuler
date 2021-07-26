def digit_sum_power(number: int, power: int) -> int:
    return sum(pow(int(digit), power) for digit in str(number))


def sum_all_numbers(power: int) -> int:
    max_length = len(str(9 ** power)) + 1
    numbers = [number for number in range(1, int("9" * max_length)) if digit_sum_power(number, power) == number]
    return sum(numbers) - 1


def main() -> None:
    assert digit_sum_power(1634, 4) == 1634
    assert digit_sum_power(8208, 4) == 8208
    assert digit_sum_power(9474, 4) == 9474
    assert sum_all_numbers(4) == 19316
    answer = sum_all_numbers(5)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

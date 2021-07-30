from fractions import Fraction
from typing import Union


def find_common_digit(num1: int, num2: int) -> Union[int, None]:
    num1_digits = set(str(num1))
    num2_digits = set(str(num2))
    common_digit = num1_digits.intersection(num2_digits).difference("0")
    return list(common_digit)


def remove_digit(number: int, digit: int) -> int:
    number_digits = list(str(number))
    digit = str(digit)
    if number_digits.count(digit) == 0:
        return int("".join(number_digits))
    elif number_digits.count(digit) == 1:
        number_digits.remove(digit)
        return int("".join(number_digits))
    else:
        return int("".join(number_digits.pop()))


def find_magical_fractions() -> list[tuple[int, int]]:
    fractions = []
    for denominator in range(10, 100):
        for nominator in range(11, denominator):
            common_digits = find_common_digit(nominator, denominator)
            if common_digits:
                nominator_new = remove_digit(nominator, common_digits[0])
                denominator_new = remove_digit(denominator, common_digits[0])
                try:
                    if nominator / denominator == nominator_new / denominator_new:
                        fractions.append((nominator, denominator))
                except ZeroDivisionError:
                    pass
    return fractions


def calculate_answer(fractions: list[tuple[int, int]]) -> int:
    nominator, denominator = 1, 1
    for fraction in fractions:
        nominator = nominator * fraction[0]
        denominator = denominator * fraction[1]
    return Fraction(nominator, denominator).denominator


def main() -> None:
    fractions = find_magical_fractions()
    answer = calculate_answer(fractions)
    print(f"Answer: {answer}")
           

if __name__ == "__main__":
    main()

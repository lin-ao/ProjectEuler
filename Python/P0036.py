from typing import Generator


def is_palindrome(number: int) -> bool:
    digits = list(str(number))
    if len(digits) & 1 == 0:
        return digits[:(len(digits) // 2)] == list(reversed(digits[(len(digits) // 2):]))
    else:
        return digits[:(len(digits) // 2)] == list(reversed(digits[(len(digits) // 2 + 1):]))


def find_double_palindromes(threshold: int) -> Generator[int, None, None]:
    for number in range(threshold):
        binary = bin(number)[2:]
        if is_palindrome(number) and is_palindrome(binary):
            yield number


def main() -> None:
    answer = sum(find_double_palindromes(1000000))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

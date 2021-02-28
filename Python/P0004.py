def is_palindrome(number: int) -> bool:
    digits = list(str(number))
    if len(digits) & 1 == 0:
        return digits[:(len(digits) // 2)] == list(reversed(digits[(len(digits) // 2):]))
    else:
        return digits[:(len(digits) // 2)] == list(reversed(digits[(len(digits) // 2 + 1):]))


def find_products(digits: int) -> list[int]:
    largest = int("".join(["9"] * digits))
    return [x * y for x in range(1, largest + 1) for y in range(1, largest + 1)]


def find_largest(products: list[int]) -> int:
    return max(filter(is_palindrome, products))


def main() -> None:
    assert find_largest(find_products(2)) == 9009
    answer = find_largest(find_products(3))
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()

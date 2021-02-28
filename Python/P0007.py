def is_prime(number: int) -> bool:
    if number == 2:
        return True
    elif number < 2 or number & 1 == 0:
        return False
    else:
        return not any(number % i == 0 for i in range(2, number // 3 + 1))


def nth_prime(n: int) -> int:
    number = 2
    found = 0
    while True:
        if is_prime(number):
            found += 1
        if found == n:
            return number
        number += 1


def main() -> None:
    assert nth_prime(6) == 13
    answer = nth_prime(10001)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

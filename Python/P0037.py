from collections import defaultdict
from typing import Generator


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    elif number < 2 or number & 1 == 0:
        return False
    else:
        return not any(number % i == 0 for i in range(2, number // 3 + 1))


def prime_sieve() -> Generator[int, None, None]:
    composites = defaultdict(list)
    number = 2
    while True:
        if number not in composites:
            yield number
            composites[number ** 2].append(number)
        else:
            for prime in composites[number]:
                composites[number + prime].append(prime)
            del composites[number]
        number += 1


def check_right_truncates(number: int) -> bool:
    numbers = [int(str(number)[:-x]) for x in range(1, len(str(number)))]
    return all(is_prime(number) for number in numbers)


def check_left_truncates(number: int) -> bool:
    numbers = [int(str(number)[x:]) for x in range(1, len(str(number)))]
    return all(is_prime(number) for number in numbers)


def is_truncatable_prime(number: int) -> bool:
    return number > 10 and check_right_truncates(number) and check_left_truncates(number)


def find_truncatable_primes(limit: int) -> list[int]:
    found = 0
    answer = []
    for number in prime_sieve():
        if found >= limit:
            return answer
        elif is_truncatable_prime(number):
            found += 1
            answer.append(number)


def main() -> None:
    assert is_truncatable_prime(3797) == True
    answer = sum(find_truncatable_primes(11))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

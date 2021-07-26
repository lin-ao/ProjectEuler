from collections import defaultdict
from typing import Generator


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    elif number < 2 or number & 1 == 0:
        return False
    else:
        return not any(number % i == 0 for i in range(2, number // 3 + 1))


def prime_sieve(limit: int) -> Generator[int, None, None]:
    composites = defaultdict(list)
    number = 2
    while number < limit + 1:
        if number not in composites:
            yield number
            composites[number ** 2].append(number)
        else:
            for prime in composites[number]:
                composites[number + prime].append(prime)
            del composites[number]
        number += 1


def quadratic_formula(a: int, b: int, n: int) -> int:
    return int(n ** 2 + a * n + b)


def consecutive_primes(a: int, b: int, n: int = None, count: int = None) -> tuple[int, int, int]:
    if n is None:
        n = 0
    if count is None:
        count = 0
    candidate = quadratic_formula(a, b, n)
    if is_prime(candidate):
        return consecutive_primes(a, b, n + 1, count + 1)
    else:
        return (a, b, count)


def longest_consecutive(a_limit: int, b_limit: int) -> tuple[int, int, int]:
    longest = (0, 0, 0)
    for b in prime_sieve(b_limit):
        for a in range(-a_limit, a_limit + 1):
            current = consecutive_primes(a, b)
            if current[2] > longest[2]:
                longest = current
    return longest


def main() -> None:
    assert consecutive_primes(1, 41)[2] == 40
    assert consecutive_primes(-79, 1601)[2] == 80
    longest = longest_consecutive(1000, 1000)
    answer = longest[0] * longest[1]
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

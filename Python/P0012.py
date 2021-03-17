from collections import defaultdict
from functools import reduce
from operator import mul
from typing import Generator


def triangular_number() -> Generator[int, None, None]:
    sequence = {1: 1}
    count = 0
    while True:
        count += 1
        if count not in sequence:
            sequence[count] = sequence[count - 1] + count  
        yield sequence[count]


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


def smallest_prime_factor(number: int) -> int:
    for prime in prime_sieve():
        if number % prime == 0:
            return prime


def prime_factors(number: int, factors=None) -> dict[int, int]:
    if not factors:
        factors = defaultdict(lambda: 0)
    if number == 1:
        return factors
    else:
        prime_factor = smallest_prime_factor(number)
        factors[prime_factor] += 1
        return prime_factors(number / prime_factor, factors)


def count_divisors(factors: dict[int, int]) -> int:
    return reduce(mul, (num + 1 for num in factors.values()), 1)


def find_number_with_divisors(limit: int) -> int:
    for num in triangular_number():
        divisors = count_divisors(prime_factors(num))
        if divisors > limit:
            return num


def main() -> None:
    assert find_number_with_divisors(5) == 28
    answer = find_number_with_divisors(500)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

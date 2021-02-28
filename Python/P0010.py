from collections import defaultdict
from itertools import takewhile
from typing import Generator


def sieve_of_erastosthenes() -> Generator[int, None, None]:
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


def sum_primes(upper: int) -> int:
    return sum(takewhile(lambda x: x < upper, sieve_of_erastosthenes()))


def main() -> None:
    assert sum_primes(10) == 17
    answer = sum_primes(2000000)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

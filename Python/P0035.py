from collections import defaultdict, deque
from typing import Generator


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


def generate_rotations(number: int) -> list[int]:
    candidates = []
    digits = deque(list(str(number)))
    for _ in range(len(digits)):
        digits.rotate()
        candidates.append(int("".join(digits)))
    return candidates


def is_prime(primes: list[int], number: int) -> bool:
    return number in primes


def is_circular_prime(primes: list[int], candidates: list[int]) -> bool:
    return all(map(lambda x: is_prime(primes, x), candidates))


def count_circular_primes(threshold: int) -> int:
    primes = [prime for prime in prime_sieve(threshold)]
    circular_primes = set()
    while primes:
        candidates = generate_rotations(primes[0])
        if is_circular_prime(primes, candidates):
            circular_primes.update(candidates)
        for candidate in candidates:
            try:
                primes.remove(candidate)
            except ValueError:
                pass
    return len(circular_primes)


def main() -> None:
    assert count_circular_primes(100) == 13
    answer = count_circular_primes(1000000)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

def is_prime(number: int) -> bool:
    return not (number & 1 == 0 or any(number % i == 0 for i in range(3, number, 2)))


def next_prime_factor(lower: int, upper: int) -> int:
    for number in range(lower, upper + 1):
        if is_prime(number) and upper % number == 0:
            return number
    return upper


def largest_prime_factor(upper: int, lower=None) -> int:
    if lower is None:
        lower = 2
    npf = next_prime_factor(lower, upper)
    if npf == upper:
        return upper
    else:
        return largest_prime_factor(upper // npf, npf)


def main() -> None:
    assert largest_prime_factor(13195) == 29
    answer = largest_prime_factor(600851475143)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

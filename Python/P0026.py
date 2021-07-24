def calc_modulo(devisor: int, denominator: int) -> int:
    return devisor * 10 % denominator


def count_recurring(denominator: int, remainder: int = None, remainders: list[int] = None) -> int:
    if remainder is None:
        remainder = 1
    if remainders is None:
        remainders = [0]
    remainder = remainder * 10 % denominator
    if remainder == 0:
        return (denominator, 0)
    elif remainder in remainders:
        return (denominator, len(remainders) - remainders.index(remainder))
    else:
        remainders.append(remainder)
        return count_recurring(denominator, remainder, remainders)


def find_longest_recurring(limit: int) -> int:
    longest = (0, 0)
    for denominator in range(1, limit):
        current = count_recurring(denominator)
        if current[1] > longest[1]:
            longest = current
    return longest[0]


def main() -> None:
    assert find_longest_recurring(10) == 7
    answer = find_longest_recurring(1000)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

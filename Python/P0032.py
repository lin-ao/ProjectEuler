def non_duplicate(number: int) -> bool:
    digits = list(str(number))
    return len(digits) == len(set(digits).difference("0"))
 

def is_pandigital(number: int) -> bool:
    return non_duplicate(number) and len(str(number)) == 9


def count_all_pandigital() -> int:
    results = set()
    for multiplicant in range(1, 9877):
        for multiplier in range(1, 99):
            numbers = [multiplicant, multiplier, multiplicant * multiplier]
            if numbers[2] > 9876:
                break
            elif all(map(non_duplicate, numbers)) and is_pandigital("".join(map(str, numbers))):
                results.add(numbers[2])
    return sum(results)


def main() -> None:
    answer = count_all_pandigital()
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

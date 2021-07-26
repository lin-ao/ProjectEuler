def count_unique(a: int, b: int) -> int:
    uniques = set()
    for a in range(2, a + 1):
        for b in range(2, b + 1):
            uniques.add(pow(a, b))
    return len(uniques)


def main() -> None:
    assert count_unique(5, 5) == 15
    answer = count_unique(100, 100)
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()

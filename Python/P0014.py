def collatz_seq(number: int, sequence=None) -> list[int]:
    if not sequence:
        sequence = [number]
    if number == 1:
        sequence.append(number)
        return sequence
    else:
        if number & 1 == 0:
            number = number // 2
            sequence.append(number)
        else:
            number = number * 3 + 1
            sequence.append(number)
        return collatz_seq(number, sequence)


def main() -> None:
    collatz_lengths = {i: len(collatz_seq(i)) for i in range(1, 1000000)}
    answer = max(collatz_lengths, key = lambda k: collatz_lengths[k])
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

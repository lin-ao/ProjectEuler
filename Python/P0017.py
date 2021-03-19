def num_to_word(number: int) -> str:
    ones = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 
            13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    if number == 1000:
        return "one thousand"
    elif number < 20:
        return ones[number]
    elif number < 100:
        ten, one = divmod(number, 10)
        return f"{tens[ten]} {num_to_word(one)}"
    elif number % 100 == 0 and not number == 1000:
        return f"{ones[number // 100]} hundred"
    elif number < 1000:
        hundred, ten = divmod(number, 100)
        return f"{ones[hundred]} hundred and {num_to_word(ten)}"



def count_letters(word: str) -> int:
    return len(list(word.replace(" ", "")))


def main() -> None:
    assert count_letters(num_to_word(342)) == 23
    assert count_letters(num_to_word(115)) == 20
    answer = sum(count_letters(num_to_word(num)) for num in range(1, 1001))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

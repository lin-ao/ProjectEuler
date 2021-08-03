package main

import (
	"fmt"
)

func is_even(number int) bool {
	return number%2 == 0
}

func fibonacci(threshold int) chan int {
	sequence := make(chan int)
	go func() {
		x, y := 1, 1
		for x <= threshold {
			sequence <- x
			x, y = y, x+y
		}
		close(sequence)
	}()
	return sequence
}

func calculate_sum(threshold int) int {
	var sum int = 0
	for number := range fibonacci(threshold) {
		if is_even(number) {
			sum += number
		}
	}
	return sum
}

func main() {
	var threshold int = 4000000
	var answer int = calculate_sum(threshold)
	fmt.Printf("Answer: %d\n", answer)
}

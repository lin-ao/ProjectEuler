package main

import (
	"fmt"
)

func calculate_sum(threshold int, divisible_by []int) int {
	var sum int = 0
	for number := 0; number < threshold; number++ {
		var divisible bool = true
		for divisor := range divisible_by {
			divisible = divisible && number%divisor == 0
		}
		if divisible {
			sum += number
		}
	}
	return sum
}

func main() {
	var threshold int = 1000
	var divisible_by = [2]int{3, 5}
	var answer int = calculate_sum(threshold, divisible_by[:])
	fmt.Printf("Answer: %d\n", answer)
}

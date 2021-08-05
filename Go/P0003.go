package main

import (
	"fmt"
	"math"
)

func is_prime(number int) bool {
	if number%2 == 0 {
		return false
	}
	for num := 3; num < int(math.Sqrt(float64(number))); num++ {
		if number%num == 0 {
			return false
		}
	}
	return true
}

func find_prime_factors(number int) []int {
	var prime_factors []int
	for num := 2; num < int(math.Sqrt(float64(number))); num++ {
		if is_prime(num) && number%num == 0 {
			prime_factors = append(prime_factors, num)
		}
	}
	return prime_factors
}

func find_max(numbers []int) int {
	var max int = 0
	for _, number := range numbers {
		if number > max {
			max = number
		}
	}
	return max
}

func main() {
	var answer int = find_max(find_prime_factors(600851475143))
	fmt.Printf("Answer: %v\n", answer)
}

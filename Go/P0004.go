package main

import (
	"fmt"
	"strconv"
	"strings"
)

func reverse(slice []string) []string {
	slice_copy := make([]string, len(slice))
	copy(slice_copy, slice)
	for i, j := 0, len(slice_copy)-1; i < j; i, j = i+1, j-1 {
		slice_copy[i], slice_copy[j] = slice_copy[j], slice_copy[i]
	}
	return slice_copy
}

func is_pallindrome(number int) bool {
	var number_string []string = strings.Split(strconv.Itoa(number), "")
	var reversed_number []string = reverse(number_string)
	if strings.Join(number_string, "") == strings.Join(reversed_number, "") {
		return true
	} else {
		return false
	}
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

func largest_pallindrome(threshold int) int {
	var products chan int = make(chan int)
	var pallindromes []int
	go func() {
		for i := 1; i <= threshold; i++ {
			for j := 1; j <= threshold; j++ {
				products <- i * j
			}
		}
		close(products)
	}()
	for product := range products {
		if is_pallindrome(product) {
			pallindromes = append(pallindromes, product)
		}
	}
	var largest int = find_max(pallindromes)
	return largest
}

func main() {
	var answer int = largest_pallindrome(999)
	fmt.Printf("Answer: %v", answer)
}

package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	max_ := 0

	input, _ := io.ReadAll(os.Stdin)
	for _, line := range strings.Split(string(input), "\n\n") {
		acc := 0
		for _, ch := range strings.Split(line, "\n") {
			v, _ := strconv.Atoi(ch)
			acc += v
		}
		max_ = max(acc, max_)
	}

	fmt.Println("Max: ", max_)
}

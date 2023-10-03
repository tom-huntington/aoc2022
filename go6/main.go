package main

import (
	"fmt"
	"io"
	"os"
)

//s = stdin.read()
//print(next(i+4 for i in range(len(s)) if len(set(s[i:i+4])) == 4))

func main() {
	input, _ := io.ReadAll(os.Stdin)
	for i := range input {
		set := make(map[byte]bool)
		for j := range [4]int{} {
			set[input[i+j]] = true
		}
		if len(set) == 4 {
			fmt.Println(i + 4)
			break
		}
	}
}

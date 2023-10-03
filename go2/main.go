package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

//print(sum((b-a+4)%3*3+b for r in stdin.readlines() for a,b in [(ord(r[0])-64, ord(r[2])-87)]))

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	sum := 0
	for scanner.Scan() {
		r := scanner.Text()
		a, b := int(r[0])-64, int(r[2])-87
		sum += (b-a+4)%3*3 + b
	}
	fmt.Println("Sum: ", sum)
}

func crunchSplitFunc(data []byte, atEOF bool) (advance int, token []byte, err error) {

	// Return nothing if at end of file and no data passed
	if atEOF && len(data) == 0 {
		return 0, nil, nil
	}

	// Find the index of the input of a newline followed by a
	// pound sign.
	if i := strings.Index(string(data), "\n\n"); i >= 0 {
		return i + 1, data[0:i], nil
	}

	// If at end of file with data return the data
	if atEOF {
		return len(data), data, nil
	}

	return
}

package main

import (
	"bufio"
	"fmt"
	"os"
)

//def fn(s):
//    l = len(s) // 2
//    p = ord((set(s[:l])&set(s[l:])).pop())-96
//    return p + 58 if p < 0 else p
//
//print(sum(fn(s) for s in stdin.readlines()))

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	sum := 0
	for scanner.Scan() {
		t := scanner.Text()
		l := len(t) / 2
		p := func() int {
			for _, ch0 := range t[:l] {
				for _, ch1 := range t[l:] {
					if ch0 == ch1 {
						return (int(ch0) - 96 + 58) % 58
					}
				}
			}
			panic("not reached")
		}()
		sum += p
	}
	fmt.Println(sum)
}

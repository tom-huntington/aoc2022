package main

import (
	"bufio"
	"fmt"
	"os"
)

//n = map(int,findall(r'\d+',stdin.read()))
//print(sum((a==c) or (b==d) or (a<c)==(b>d) for (a,b,c,d) in zip(n,n,n,n)))

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	sum := 0
	for scanner.Scan() {
		var a, b, c, d int
		fmt.Sscanf(scanner.Text(), "%d-%d,%d-%d", &a, &b, &c, &d)
		if (a == c) || (b == d) || ((a < c) == (b > d)) {
			sum += 1
		}
	}
	fmt.Println(sum)
}

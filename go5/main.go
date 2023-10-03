package main

import (
	"fmt"
	"io"
	"os"
	"strings"
	"unicode"
)

// (i:=stdin.read().split('\n\n'))
// (m:=[[*filter(str.isalpha,s[::-1])] for c,s in enumerate(zip(*i[0].split('\n'))) if c%4==1])
// (t:=map(int,findall(r'\d+',i[1])))
// [(m[b-1].extend(m[a-1][-k:][::-1]),[m[a-1].pop() for _ in range(k)]) for k,a,b in zip(t,t,t)]
// print(''.join(x[-1] for x in m))

func main() {
	input, _ := io.ReadAll(os.Stdin)
	inputs := strings.Split(string(input), "\n\n")
	rows := strings.Split(inputs[0], "\n")
	m := make([][]int, (len(rows[0])+2)/4)
	for i := range m {
		m[i] = make([]int, 0, len(rows))
	}
	fmt.Println(len(m), len(m[0]), len(rows[0]))
	fmt.Println(inputs[0], "<------")

	for i := range rows[0] {
		for j := len(rows) - 1; j >= 0; j-- {
			ch := rows[j][i]
			if unicode.IsLetter(rune(ch)) && i%4 == 1 {
				m[(i-1)/4] = append(m[(i-1)/4], int(ch))
			}
		}
	}
	//	sum := 0
	//fmt.Println(inputs[0], m)
	for _, line := range strings.Split(strings.TrimSpace(inputs[1]), "\n") {
		var num, src, dst int
		fmt.Sscanf(line, "move %d from %d to %d", &num, &src, &dst)
		src -= 1
		dst -= 1
		fmt.Println(line, num, src, dst)
		for i := 0; i < num; i++ {
			m[dst] = append(m[dst], m[src][len(m[src])-1-i])
		}
		m[src] = m[src][:len(m[src])-num]
	}
	for _, stack := range m {
		fmt.Printf("%c", stack[len(stack)-1])
	}
	//fmt.Printf("%c", m)

}

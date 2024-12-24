package main

import (
	"fmt"
	"os"
)

func main() {
	if err := run(); err != nil {
		fmt.Fprintf(os.Stderr, "error: ", err)
		os.Exit(1)
	}
}

func run() error {
	fmt.Fprint(os.Stdout, "finished running")
	return nil
}

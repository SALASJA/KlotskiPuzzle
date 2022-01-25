"""
This program can accept a command line argument for the dimensions.
example: python3 main.py 4
"""

from klotski import Klotski
import sys

def main():
	dimension = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isnumeric() else 3
	puzzle = Klotski(dimension)
	puzzle.shuffle()
	print(puzzle)
	while not puzzle.solved():
		choice = int(input("Enter number to shift: "))
		puzzle.shift(choice)
		print(puzzle)
		

main()
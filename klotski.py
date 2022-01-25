import math

class Klotski:
	"""
	available functions:
		__init__
		to_grid_string
		__str__
		__repr__
		shift
		solved
		shuffle
		reset
	"""
	def __init__(self, dimension = 3):
		"""
			Accepts a positive integer argument for the dimension, 
			where it makes a demension x dimension grid/
			The default value is 3. If dimension value is less than 3, 
			It defaults to 3.
		"""
		dimension = dimension if dimension >= 3 else 3
		self._grid = [[ str(j + 1) for j in range(i * dimension, i * dimension + dimension)] for i in range(dimension)]
		self._freespace_row = dimension - 1
		self._freespace_column = dimension - 1
		
	
	def to_grid_string(self):
		"""Returns a string representing the klotski puzzle."""
		dimension = len(self._grid)
		padding = math.ceil(math.log(dimension,10)) + 3
		format_string = "{:" + str(padding) + "s}"
		result = ""
		for row in self._grid:
			for number in row:
				result += format_string.format(number if number != str(dimension ** 2) else ' ')
			result += "\n\n"
				
		return result
		
	def __str__(self):
		"""
			Returns a string representing the klotski puzzle
		 	as well as a listing of which numbers can be shifted.
		"""
		grid_string = self.to_grid_string()
		return grid_string
	
	def __repr__(self):
		"""Useful when running in the python interpreter, returns the result of __str__."""
		return self.__str__()
		
	def shift(self, choice):
		"""
			Shifts a given choice if a valid integer, altering the freespace position. 
			Returns true if number shifting successful otherwise
			false if it wasn't a successful shift.
		'"""
		return False
	
	def solved(self):
		"""
			Returns true if grid is solved, for example, in a 3x3 grid (aka dimension 3) 
			the following is a solved grid:
			
			1 2 3
			4 5 6
			7 8 
			
			Note: the 9 is a freespace so it is omitted.
		
		"""
		count = 1
		for i in range(len(self._grid)):
			for j in range(len(self._grid[0])):
				if self._grid[i][j] != str(count):
					return False
				count = count + 1
		return True
	
	def shuffle(self):
		"""shuffles the grid using the shift function"""
		pass
	
	def reset(self):
		"""resets grid to original state"""
		dimension = len(self._grid)
		self._grid = [[ str(j + 1) for j in range(i * dimension, i * dimension + dimension)] for i in range(dimension)]
		self._freespace_row = dimension - 1
		self._freespace_column = dimension - 1
		
	
	
		
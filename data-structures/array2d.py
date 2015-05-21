# -----------------------------------------------------------
# demonstrates how to create and use an 2d array
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

class Array:
	def __init__(self, size):
		"constructor class to initiate this object"

		# set array size, and init the array
		self.size = size
		self.data = [None] * size

		return

	def getLength(self):
		"return the number of items"
		return self.size

	def setElementValue(self, position, value):
		"set the element value at position"
		if position in range(self.getLength()):
			self.data[position] = value
			return True
		else:
			return False

	def getElementValue(self, position):
		"get the element value at position"
		if position in range(self.getLength()):
			return self.data[position]
		else:
			return False
	
	def print(self):
		"output the elements one after the other"
		#for position in range(self.getLength()):
		#	value = self.getElementValue(position)
		#	print (value)
		print (self.data)
		
		return

class Array2D:
	def __init__(self, rows, columns):
		"constructor class to initiate this object"

		# set array size
		self.rows = rows
		self.columns = columns

		# define array to keep the rows
		self.arrayData = Array(rows)
		
		# fill each row entry with an array that represents the columns
		for currentRow in range(self.arrayData.getLength()):
			arrayRow = Array(columns)
			self.arrayData.setElementValue(currentRow, arrayRow)

		return
	
	def getSize(self):
		"return the size of the 2d array"
		return (self.rows, self.columns)

	def print(self):
		"output the array 2d content"
		for currentRow in range(self.arrayData.getLength()):
			arrayRow = self.arrayData.getElementValue(currentRow)
			arrayRow.print()
		return

# main program

# define basic array of size 3
array1 = Array(3)
print ("array length:", array1.getLength())

# set values: element 1:5
array1.setElementValue(1, 5)

# output list
array1.print()

# define 2d array of size 3x3
array2 = Array2D(3,3)
print ("2D array size:", array2.getSize())
array2.print()

"""
A dynamic array is similar to an array, but with the difference that its size can be dynamically modified at runtime.
Don’t need to specify how much large an array beforehand.
The elements of an array occupy a contiguous block of memory, and once created, its size cannot be changed.
A dynamic array can, once the array is filled, allocate a bigger chunk of memory,
copy the contents from the original array to this new space, and continue to fill the available slots.

"""
import  ctypes

class DyanamicArray(object):
	"""
	Dyanamic array class simillar to to Python list
	"""
	def __init__(self):
		self.n = 0 # Count actual elements, defaults is set to 0
		self.capacity = 1 # default capacity
		self.A = self.make_array(self.capacity)

	def __len__(self):
		"""
		Returns number of element in the array
		"""
		return self.n

	def __getitem__(self, k):
		"""
		Returns element at index k
		"""
		if 0 <= k <= self.n:
			return self.A[k]
		else:
			raise IndexError("Array out of Bounds!")

	def append(self, item):
		"""
		Add element to the end of the array
		"""
		if self.n == self.capacity:
			# if the capacity is not enough, Just fucking double it
			self._resize(2 * self.capacity)

		# setting the new item to last position of the array
		self.A[self.n] = item
		self.n += 1

	def _resize(self, new_capacity):
		"""
		doubles the capacity of the array
		"""
		B = self.make_array(new_capacity) # first make a array double the size of existing

		# next copy all the value from previous array to new one
		for k in range(self.n):
			B[k] = self.A[k]

		self.A = B # replace the old array with new one
		self.capacity = new_capacity # updates the capacity with new capacity

	def make_array(self, capacity):
		"""
		creates and return a new array with provided capacity
		"""
		return (capacity * ctypes.py_object) ()


arr = DyanamicArray()
arr.append(1)
arr.append(2)
arr.append(3)

print(arr[1])
#data types
#boolean is separated

class NumberNode:
	def __init__(self, x):
		try:
			if x.isdigit():
				self.value = int(x)
			else:
				self.value = float(x)
		except ValueError:
			print("Number error : %d", t.value)
			x = 0

	def evaluate(self):
		return self.value

class StringNode:
	def __init__(self, x):
		self.value = x[1:-1]

	def evaluate(self):
		return self.value

class TrueNode:
	def __init__(self, x):
		self.value = True

	def evaluate(self):
		return self.value

class FalseNode:
	def __init__(self, x):
		self.value = False

	def evaluate(self):
		return self.value
from error import *

def isInt(A):
	for x in A:
		if type(x.evaluate()) == int:
			continue
		else:
			return False
	return True

def isNumber(A):
	for x in A:
		if type(x.evaluate()) in {int, float} and type(x.evaluate()) in {int, float}:
			continue
		else:
			return False
	return True

def isString(S):
	for s in S:
		if isinstance(s.evaluate(), str):
			continue
		else:
			return False
	return True

def isList(L):
	for l in L:
		if isinstance(l.evaluate(), list):
			continue
		else: 
			return False
	return True

def isBool(X):
	for x in X:
		if type(x.evaluate()) == bool:
			continue
		else:
			return False
	return True


#AST nodes
class BinopNode:
	def __init__(self, t):
		self.x, self.op, self.y = t[1], t[2], t[3]

	def evaluate(self):
		if self.op == '+':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]) or isList([self.x, self.y]):
				return self.x.evaluate() + self.y.evaluate()
			else:
				raise SemanticError()

		elif self.op == '-':	
			if isNumber([self.x, self.y]):
				return self.x.evaluate() - self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '*':
			if isNumber([self.x, self.y]):
				return self.x.evaluate() * self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '/':
			if isNumber([self.x, self.y]) and self.y.evaluate() != 0:
				return self.x.evaluate()/self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '**':
			if isNumber([self.x, self.y]):
				return self.x.evaluate()**self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == 'div':
			if isInt([self.x, self.y]) and self.y.evaluate() != 0:
				return self.x.evaluate()//self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == 'mod':
			if isInt([self.x, self.y]) and self.y.evaluate() != 0:
				return self.x.evaluate() % self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == 'in':
			if isString([self.x, self.y]) or isList([self.y]):
				return self.x.evaluate() in self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '::':
			if isList([self.y]):
				y = self.y.evaluate()
				y.insert(0, self.x.evaluate())
				return y
			else:
				raise SemanticError()
		elif self.op == '<':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]):
				return self.x.evaluate() < self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '<=':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]):
				return self.x.evaluate() <= self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '>':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]):
				return self.x.evaluate() > self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '>=':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]):
				return self.x.evaluate() >= self.y.evaluate()
			else:
				raise SemanticError()

		elif self.op == '==':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]):
				return self.x.evaluate() == self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == '<>':
			if isNumber([self.x, self.y]) or isString([self.x, self.y]):
				return self.x.evaluate() != self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == 'andalso':
			if isBool([self.x, self.y]):
				return self.x.evaluate() and self.y.evaluate()
			else:
				raise SemanticError()
		elif self.op == 'orelse':
			if isBool([self.x, self.y]):
				return self.x.evaluate() or self.y.evaluate()
			else:
				raise SemanticError()


class UnaryNode:
	def __init__(self,t):
		self.op, self.x = t[1], t[2]

	def evaluate(self):
		if self.op == '-':
			if isNumber([self.x]):
				return -self.x.evaluate()
			else:
				raise SemanticError()
		else:
			raise SemanticError()

class NotNode:
	def __init__(self,t):
		self.op, self.x = t[1], t[2]

	def evaluate(self):
		if self.op == 'not':
			if isBool([self.x]):
				return not self.x.evaluate()
			else:
				raise SemanticError()
		else:
			raise SemanticError()

class IndexNode:
	def __init__(self,t):
		self.x, self.y = t[1], t[3]

	def evaluate(self):
		if (isString([self.x]) or isList([self.x])) and type(self.y.evaluate()) == int:
			try:
				return self.x.evaluate()[self.y.evaluate()]
			except Exception:
				raise SemanticError('Index out of range')
		else:
			raise SemanticError()

class ListNode:
	def __init__(self,t,empty=False):
		if not empty:
			self.value = [t[1]]
		else:
			self.value = []

	def evaluate(self):
		temp = []
		for e in self.value:
			if type(e) in {list,tuple}:
				temp.append(e)
			else:
				temp.append(e.evaluate())
		return temp

	def addNode(self, x):
		self.value.append(x)


class TupleNode:
	def __init__(self,t,empty=False):
		if not empty:
			self.value = [t[1]]
		else:
			self.value = []

	def evaluate(self):
		temp = []
		for e in self.value:
			if type(e) is list:
				temp.append(e)
			else:
				temp.append(e.evaluate())
		return tuple(temp)

	def addNode(self, x):
		self.value.append(x)

class TupleIndex:
	def __init__(self, t):
		self.x, self.y = t[3], t[2]

	def evaluate(self):
		if type(self.x.evaluate()) == tuple and type(self.y.evaluate()) == int:
			try:
				return self.x.evaluate()[self.y.evaluate()-1]
			except Exception:
				raise SemanticError('Index out of range')
		else:
			raise SemanticError('Invalid call')

#error
class SyntaxError(Exception):
	def __init__(self, msg = "some syntax error"):
		super().__init__(msg)
class SemanticError(Exception):
	def __init__(self, msg = 'some semantic error'):
		super().__init__(msg)
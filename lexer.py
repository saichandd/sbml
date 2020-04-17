from data_nodes import *

tokens = (
	'LPAREN', 'RPAREN',
	'LBRACKET', 'RBRACKET',
	'COMMA', 
	'TUPLE_INDEX', 
	'PLUS', 'MINUS', 'TIMES', 'EXPONENT', 'DIVIDE', 'DIV', 'MOD',
	'IN', 'CONS',
	'LESS_THAN', 'GREATER_THAN', 'LESS_EQUAL', 'GREATER_EQUAL',
	'EQUAL', 'NOT_EQUAL',  'NOT', 'ANDALSO', 'ORELSE',
	'TRUE', 'FALSE', 'STRING',
	'NUMBER'
	# 'INTEGER','REAL'
)


# reserved = { t.lower(): t for t in tokens}

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_TUPLE_INDEX = r'\#'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EXPONENT = r'\*\*'
t_DIVIDE = r'/'
t_DIV = r'div'
t_MOD = r'mod'
t_IN = r'in'
t_CONS = r'\:\:'
t_LESS_THAN = r'\<'
t_GREATER_THAN = r'\>'
t_LESS_EQUAL = r'\<\='
t_GREATER_EQUAL = r'\>\='
t_EQUAL = r'=='
t_NOT_EQUAL = r'\<\>'
t_NOT = r'not'
t_ANDALSO = r'andalso'
t_ORELSE = r'orelse'

def t_TRUE(t):
	r'True'
	t.value = TrueNode(t.value)
	return t
def t_FALSE(t):
	r'False'
	t.value = FalseNode(t.value)
	return t

# def t_INTEGER(t):
# 	r'([0-9]([0-9])*)'
# 	try:
# 		t.value = int(t.value)
# 	except ValueError:
# 		print('Intger value error: %d', t.value)
# 	return t

# def t_REAL(t):
#     r'(([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+))([eE][+-]?[0-9]+)?'
#     try:
#         t.value = float(t.value)
#     except ValueError:
#         print("Real number error : %d", t.value)
#         t.value = 0.0
#     return t

def t_NUMBER(t):
	r'(([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+))([eE][+-]?[0-9]+)?|([0-9]([0-9])*)'
	t.value = NumberNode(t.value)

	return t

def t_STRING(t):
	r'''(\"([^\\\"]|\\.)*\")|(\'([^\\\']|\\.)*\')'''
	t.value = StringNode(t.value)
	return t



#boilerplate stuff
def t_newline(t):
	r'\n+'

t_ignore = " \t"

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

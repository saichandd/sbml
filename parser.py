from ast import *
# Parsing rules
precedence = (
	('left', 'ORELSE'),
	('left', 'ANDALSO'),
	('left', 'NOT'),
	('left', 'LESS_THAN'), ('left', 'LESS_EQUAL'), ('left', 'EQUAL'), ('left', 'NOT_EQUAL'), ('left', 'GREATER_THAN'), ('left', 'GREATER_EQUAL'),
	('right', 'CONS'),
	('left', 'IN'),
	('left', 'PLUS'), ('left', 'MINUS'),
	('left', 'TIMES'), ('left', 'DIVIDE'), ('left', 'DIV'), ('left', 'MOD'),
	('right', 'EXPONENT'),
	('right', 'UMINUS'),
	('left', 'LBRACKET', 'RBRACKET'),
	('left', 'TUPLE_INDEX'),
	('left', 'LPAREN', 'RPAREN')
)

#define production
def p_statement_expression(t):
	'statement : expression'
	print(t[1].evaluate())

def p_expression_binop(t):
	'''expression : expression PLUS expression
					| expression MINUS expression
					| expression TIMES expression
					| expression DIVIDE expression
					| expression EXPONENT expression
					| expression DIV expression
					| expression MOD expression
					| expression IN expression
					| expression CONS expression
					| expression LESS_THAN expression
					| expression LESS_EQUAL expression
					| expression EQUAL expression
					| expression NOT_EQUAL expression
					| expression GREATER_THAN expression
					| expression GREATER_EQUAL expression
					| expression ANDALSO expression
					| expression ORELSE expression'''

	t[0] = BinopNode(t)

def p_expression_term(t):
	'''expression : NUMBER
					| STRING
					| TRUE
					| FALSE
					| index
					| list
					| tuple
					| TUPLE_INDEX'''
	t[0] = t[1]

def p_expression_expression(t):
	'expression : LPAREN expression RPAREN'
	t[0] = t[2]

def p_expression_unary(t):
	'expression : MINUS expression %prec UMINUS'
	t[0] = UnaryNode(t)

def p_expression_negate(t):
	'expression : NOT expression'
	t[0] = NotNode(t)

def p_expression_index(t):
    'index : expression LBRACKET expression RBRACKET'
    t[0] = IndexNode(t)

def p_hash_index(t):
    'index : TUPLE_INDEX expression tuple'
    t[0] = TupleIndex(t)

def p_list(t):
	'list : LBRACKET inlist RBRACKET'
	t[0] = t[2]

def p_list_empty(t):
	'list : LBRACKET RBRACKET'
	t[0] = ListNode(t, True)

def p_inlist(t):
	'inlist : expression'
	t[0] = ListNode(t)

def p_inlist_comma_expression(t):
	'inlist : inlist COMMA expression'
	t[1].addNode(t[3])
	t[0] = t[1]

def p_tuple(t):
	'tuple : LPAREN intuple RPAREN'
	t[0] = t[2]

def p_tuple_empty(t):
	'tuple : LPAREN RPAREN'
	t[0] = TupleNode(t, True)

def p_intuple(t):
	'intuple : expression'
	t[0] = TupleNode(t)

def p_intuple_comma_expression(t):
	'intuple : intuple COMMA expression'
	t[1].addNode(t[3])
	t[0] = t[1]

def p_intuple_comma(t):
	'intuple : intuple COMMA'
	t[0] = t[1]

def p_error(t):
	raise SyntaxError('error while building parse tree')

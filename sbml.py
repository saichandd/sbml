#-------------------------------------
#Name: Sai Chand Duppala 
#ID: 112684112
#
#Run: run this in python3 with txt file as argument
#
#-------------------------------------

import ply.lex as lex
import ply.yacc as yacc
import sys

from lexer import *
from parser import *


if __name__ == '__main__':

	# Build the lexer
	lexer = lex.lex()

	#build the parser
	yacc.yacc(debug=0)

	if len(sys.argv) != 2:
		sys.exit("invalid number of arguments")

	file_descriptor = open(sys.argv[1], 'r')

	for line in file_descriptor:
		expression = line.strip()
		try:
			lex.input(expression)
			while True:
				token = lex.token()
				if not token:
					break
			ast = yacc.parse(expression)
		except SyntaxError:
			print("Syntax Error")	
		except SemanticError:
			print("Semantic Error")
		
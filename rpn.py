#!/usr/bin/env python3

import sys
import operator
from termcolor import colored, cprint

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}

OPERATOR_COLOR = {
	'+': "magenta",
	'-': "white",
	'*': "blue",
	'/': "yellow",
	'^': "cyan",
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			interOut = str(arg1) + str(operand) + str(arg2) + " = " + str(result)
			if result < 0:
				cprint(interOut, OPERATOR_COLOR[operand], 'on_red')
			else:
				cprint(interOut, OPERATOR_COLOR[operand])
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		if result < 0:
			cprint('Result: ' + str(result) , 'green', 'on_red')
		else:
			cprint('Result: ' + str(result) , 'green')

if __name__ == '__main__':
	main()

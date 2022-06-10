#!/usr/bin/env python3

import os
import re
import operator


def validate_input(expression):
  template = '^(\d+(\+|-|\*|\/|\^))+\d+$'

  return re.match(template, expression) is not None


def parse_expression(expression):
  template = '\+|-|/|\*|\^'

  operands = re.split(template, expression)
  operands = [int(operand) for operand in operands]

  operators = re.findall(template, expression)

  return operands, operators


def operate(op, operands, operators, i):
  operands[i] = op(operands[i], operands[i + 1])
  operands.pop(i + 1)
  operators.pop(i)


def calc_level(level_ops, operands, operators):
  i = 0
  while i < len(operators):
    skiped = True
    for symb, op in level_ops:
      if operators[i] == symb:
        operate(op, operands, operators, i)
        skiped = False
        break
    if skiped:
      i += 1


def calculate(expression):
  operands, operators = parse_expression(expression)

  op_levels = [
    [
      ('*', operator.imul),
      ('/', operator.itruediv),
      ('^', operator.ipow),
    ],
    [
      ('+', operator.iadd),
      ('-', operator.isub),
    ],
  ]

  for op_level in op_levels:
    calc_level(op_level, operands, operators)

  return operands[0]


if __name__ == '__main__':
  expression = input('Please input mathematical expression: ')
  if not validate_input(expression):
    print('error: invalid expression')
    os._exit(1)

  result = calculate(expression)
  print(f'result = {result}')

  os._exit(0)


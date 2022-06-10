#!/usr/bin/env python3

import unittest
import pycalc


class TestCalc(unittest.TestCase):

  def test_validate_input(self):
    testdata = [
      ('1*2+3/4',   True),
      ('123+321',   True),
      ('/6889-789', False),
      ('12*-34',    False),
      ('12+',       False),
      ('-+/8',      False),
      ('1.2+3.4',   False),
      ('0,1-0,2',   False),
    ]
    for expression, result in testdata:
      self.assertEqual(pycalc.validate_input(expression), result)


  def test_parse_expression(self):
    testdata = [
      ('123*234+345/5', ([123, 234, 345, 5], ['*', '+', '/'])),
      ('1*2+3/5',       ([1, 2, 3, 5],       ['*', '+', '/'])),
      ('123',           ([123],              [])),
    ]
    for expression, (operands, operations) in testdata:
      self.assertEqual(pycalc.parse_expression(expression), (operands, operations))


  def test_calculate(self):
    testdata = [
      ('21*2',      42),
      ('12*3/2',    18),
      ('3+2*4-6/3', 9),
      ('3/2',       1.5),
      ('2^3*5-18',  22),
      ('5+3^2-8',   6),
    ]
    for expression, result in testdata:
      self.assertEqual(pycalc.calculate(expression), result)


if __name__ == '__main__':
  unittest.main()


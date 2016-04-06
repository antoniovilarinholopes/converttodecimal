import unittest

import baseconverter as bctr

class Test12(unittest.TestCase):
  tests = []
  results = []
  base = 12

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)

    converter = bctr.DecimalBaseConverter("C",self.base)
    with self.assertRaises(bctr.InvalidDigitForBaseException) as context:
      converter.convert()
    self.assertTrue("invalid digits" in "".join(context.exception))

  def setUp(self):       
    converter = bctr.DecimalBaseConverter("9",self.base)
    self.tests.append(converter)
    self.results.append(9)
    converter = bctr.DecimalBaseConverter("B",self.base)
    self.tests.append(converter)
    self.results.append(11)
    converter = bctr.DecimalBaseConverter("10",self.base)
    self.tests.append(converter)
    self.results.append(12)
    converter = bctr.DecimalBaseConverter("100000",self.base)
    self.tests.append(converter)
    self.results.append(248832)
         

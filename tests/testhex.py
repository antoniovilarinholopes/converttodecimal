import unittest

import baseconverter as bctr

class TestHex(unittest.TestCase):
  tests = []
  results = []
  base = 16  

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)

    converter = bctr.DecimalBaseConverter("G",15)
    with self.assertRaises(bctr.InvalidDigitForBaseException) as context:
      converter.convert()
    self.assertTrue("invalid digits" in "".join(context.exception))

  def setUp(self):       
    converter = bctr.DecimalBaseConverter("F",self.base)
    self.tests.append(converter)
    self.results.append(15)
    converter = bctr.DecimalBaseConverter("10",self.base)
    self.tests.append(converter)
    self.results.append(16)
    converter = bctr.DecimalBaseConverter("1E",self.base)
    self.tests.append(converter)
    self.results.append(30)
    converter = bctr.DecimalBaseConverter("21",self.base)
    self.tests.append(converter)
    self.results.append(33)
         

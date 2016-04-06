import unittest

import baseconverter as bctr

class TestOctal(unittest.TestCase):
  tests = []
  results = []
  base = 8
  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)

    converter = bctr.DecimalBaseConverter("8",self.base)
    with self.assertRaises(bctr.InvalidDigitForBaseException) as context:
      converter.convert()
    self.assertTrue("invalid digits" in "".join(context.exception))

  def setUp(self):       
    converter = bctr.DecimalBaseConverter("7",self.base)
    self.tests.append(converter)
    self.results.append(7)
    converter = bctr.DecimalBaseConverter("10",self.base)
    self.tests.append(converter)
    self.results.append(8)
         

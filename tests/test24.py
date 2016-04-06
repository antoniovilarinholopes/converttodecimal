import unittest

import baseconverter as bctr

class Test24(unittest.TestCase):
  tests = []
  results = []
  base = 24
  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)

    converter = bctr.DecimalBaseConverter("O",self.base)
    with self.assertRaises(bctr.InvalidDigitForBaseException) as context:
      converter.convert()
    self.assertTrue("invalid digits" in "".join(context.exception))

  def setUp(self):       
    converter = bctr.DecimalBaseConverter("F",self.base)
    self.tests.append(converter)
    self.results.append(15)
    converter = bctr.DecimalBaseConverter("G",self.base)
    self.tests.append(converter)
    self.results.append(16)
    converter = bctr.DecimalBaseConverter("N",self.base)
    self.tests.append(converter)
    self.results.append(23)
         

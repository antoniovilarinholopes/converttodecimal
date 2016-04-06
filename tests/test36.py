import unittest

import baseconverter as bctr

class Test36(unittest.TestCase):
  tests = []
  results = []
  base = 36

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)

    converter = bctr.DecimalBaseConverter("_",self.base)
    with self.assertRaises(bctr.NotAllNumCharsException) as context:
      converter.convert()
    self.assertTrue("Invalid digit" in "".join(context.exception))

  def setUp(self):       
    converter = bctr.DecimalBaseConverter("F",self.base)
    self.tests.append(converter)
    self.results.append(15)
    converter = bctr.DecimalBaseConverter("1E",self.base)
    self.tests.append(converter)
    self.results.append(50)
    converter = bctr.DecimalBaseConverter("21",self.base)
    self.tests.append(converter)
    self.results.append(73)
         

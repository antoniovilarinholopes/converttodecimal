import unittest

import baseconverter

class Test12(unittest.TestCase):
  tests = []
  results = []
  base = 12

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("9",self.base)
    self.tests.append(converter)
    self.results.append(9)
    converter = baseconverter.DecimalBaseConverter("B",self.base)
    self.tests.append(converter)
    self.results.append(11)
    converter = baseconverter.DecimalBaseConverter("10",self.base)
    self.tests.append(converter)
    self.results.append(12)
    converter = baseconverter.DecimalBaseConverter("100000",self.base)
    self.tests.append(converter)
    self.results.append(248832)
         

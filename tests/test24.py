import unittest

import baseconverter

class Test24(unittest.TestCase):
  tests = []
  results = []
  base = 24
  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("F",self.base)
    self.tests.append(converter)
    self.results.append(15)
    converter = baseconverter.DecimalBaseConverter("G",self.base)
    self.tests.append(converter)
    self.results.append(16)
    converter = baseconverter.DecimalBaseConverter("N",self.base)
    self.tests.append(converter)
    self.results.append(23)
         

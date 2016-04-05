import unittest

import baseconverter

class Test36(unittest.TestCase):
  tests = []
  results = []

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("F",36)
    self.tests.append(converter)
    self.results.append(15)
    converter = baseconverter.DecimalBaseConverter("1E",36)
    self.tests.append(converter)
    self.results.append(50)
    converter = baseconverter.DecimalBaseConverter("21",36)
    self.tests.append(converter)
    self.results.append(73)
         

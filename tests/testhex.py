import unittest

import baseconverter

class TestHex(unittest.TestCase):
  tests = []
  results = []

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)

#    converter = baseconverter.DecimalBaseConverter("G",15)
#    self.assertRaises(Exception, converter.convert())

  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("F",15)
    self.tests.append(converter)
    self.results.append(15)
    converter = baseconverter.DecimalBaseConverter("1E",15)
    self.tests.append(converter)
    self.results.append(29)
    converter = baseconverter.DecimalBaseConverter("21",15)
    self.tests.append(converter)
    self.results.append(31)
         

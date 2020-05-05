from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    self.assertIsNone(AIchat.getQues())

if __name__=='__main__':
  unittest.main(exit=False)
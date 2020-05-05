from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite understand on  what you ask about that news.",
                     "Can you be more specific on your inquiry?"]
    testMessage = "news about the rankings?"
    arrMessage = AIchat.convert(self, testMessage)
    self.assertIn(AIchat.news(self,arrMessage),fallbackOptions)

if __name__=='__main__':
  unittest.main(exit=False)
from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    fallbackOptions = ["Can you please be more specific on the class of the professor you're asking?",
        "I can't seem to find the name of the professor you're asking.",
        "Please make sure the name of the professor is correct."]

    testMessage = "What is prof schedule"
    arrMessage = AIchat.convert(self, testMessage)
    self.assertIn(AIchat.profSched(self,arrMessage),fallbackOptions)

if __name__=='__main__':
  unittest.main(exit=False)
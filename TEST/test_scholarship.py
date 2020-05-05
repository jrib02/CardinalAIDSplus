from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite get what you're asking about scholarships.",
                     "Can you be more specific on scholarships?"]
    testMessage = "Contact number of eece department"
    arrMessage = AIchat.convert(self, testMessage)
    self.assertIn(AIchat.scholarship(self, arrMessage),fallbackOptions)

if __name__=='__main__':
  unittest.main(exit=False)
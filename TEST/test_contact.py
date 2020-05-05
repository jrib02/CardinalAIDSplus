from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
      fallbackOptions = ["Can you be more specific for me?",
      "I don't quite understand on  what you ask about the email/contact number of your desired department.",
      "Can you be more specific on your inquiry?"]

      testMsg = "contact"
      arrMessage = AIchat.convert(self,testMsg)

      self.assertIn(AIchat.contact(self,arrMessage),fallbackOptions)
if __name__=='__main__':
  unittest.main(exit=False)
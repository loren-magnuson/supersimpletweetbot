from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_new_user_directed_to_login(self):
        # The new visitor should be prompted to authenticate via twitter
        self.browser.get('http://localhost:8000')

        self.assertIn('SuperSimpleTweetBot - Login', self.browser.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()


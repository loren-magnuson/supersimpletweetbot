from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_new_user_directed_to_login(self):
        # Bonnie arrives at the home page and is prompted to authenticate via twitter
        self.browser.get('http://localhost:8000')

        self.assertIn('SuperSimpleTweetBot - Login', self.browser.title)

        self.assertIsNotNone(self.browser.find_element(By.ID, "twitter_login_link"))

        self.assertIn('SuperSimpleTweetBot - Login', self.browser.title)

    def test_new_user_can_navigate_to_twitter_login_confirmation(self):
        # Bonnie decides to click login and arrives at a confirmation page,
        # explaining they'll be logging to our app via twitter next
        # and prompted to continue on to twitter for the next step.

        self.browser.get('http://localhost:8000')

        link = self.browser.find_element(By.ID, "twitter_login_link")
        link.click()

        self.assertTrue(self.browser.current_url.endswith('/accounts/twitter/login/'))

    def test_new_user_is_redirected_after_twitter_login(self):

        self.fail('to do next')


if __name__ == '__main__':
    unittest.main()


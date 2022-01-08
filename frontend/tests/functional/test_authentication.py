from django.contrib.auth.models import User
from django.test import TestCase, Client
from selenium import webdriver
from selenium.webdriver.common.by import By


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_new_user_directed_to_login(self):
        # Bonnie arrives at the home page and is prompted to authenticate via twitter
        self.browser.get('http://localhost:8000')

        self.assertIn('SuperSimpleTweetBot - Login', self.browser.title)

        self.assertIsNotNone(self.browser.find_element(By.ID, "twitter_login_link"))

    def test_new_user_can_navigate_to_twitter_login_confirmation(self):
        # Bonnie decides to click login and arrives at a confirmation page,
        # explaining they'll be logging to our app via twitter next
        # and prompted to continue on to twitter for the next step.

        self.browser.get('http://localhost:8000')

        link = self.browser.find_element(By.ID, "twitter_login_link")
        link.click()

        self.assertTrue(self.browser.current_url.endswith('/accounts/twitter/login/'))

    def test_authenticated_user_is_sent_to_homepage(self):
        credentials = {
            'username': 'test',
            'password': 'test'
        }

        user = User.objects.create(username=credentials['username'])
        user.set_password(credentials['password'])
        user.save()

        c = Client()
        c.login(username=credentials['username'], password=credentials['password'])

        response = c.get('http://127.0.0.1:8000')
        response.render()

        self.assertIn('SuperSimpleTweetBot - Home', str(response.content))

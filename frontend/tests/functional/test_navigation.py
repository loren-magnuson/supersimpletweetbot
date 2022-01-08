from django.contrib.auth.models import User
from django.test import TestCase, Client
from selenium import webdriver
from selenium.webdriver.common.by import By


class WhoisUserTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_navigation_items(self):
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

        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)


        self.assertIn('SuperSimpleTweetBot - Home', str(response.content))

        navigation = self.browser.find_element(By.ID, "main_nav")

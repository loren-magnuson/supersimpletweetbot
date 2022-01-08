# from django.contrib.auth.models import User
# from django.test import TestCase, Client
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class WhoisUserTest(TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Chrome()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_user_can_reach_whois_page(self):
#         # Bonnie arrives at the home page after authenticating
#         # The option to perform a "whois lookuP" is presented
#         # Clicking the option leads Bonnie to a page with a Twitter user search box
#
#         self.browser.get('http://127.0.0.1:8000')
#
#         self.assertIsNotNone(self.browser.find_element(By.ID, "twitter_user_search"))

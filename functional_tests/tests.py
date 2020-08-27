from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,
                              [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_a_list_start_for_one_user(self):
        # Go visit the site
        self.browser.get(self.live_server_url+'/lists/')

        # Notice that it's a To-Do app from the title and the headeer
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # They are directly prompted to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Types "Finish the briding coursework" into the text box
        inputbox.send_keys('Finish the bridging coursework')

        # On hitting enter the page updates and the lists '1. Finish the bridging coursework'
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Finish the bridging coursework')

        # There is a text box inviting them to add another item
        # Adds "Submit coursework"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Submit the coursework')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1. Finish the bridging coursework')
        self.wait_for_row_in_list_table('2. Submit the coursework')

        # Satisfied

    def test_multiple_users_can_start_lists_at_differen_urls(self):

        # Bob comes to the website adds an item to list
        self.browser.get(self.live_server_url + '/lists/')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Do something cool')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Do something cool')

        # notices that her list has a unique url
        bob_list_url = self.browser.current_url
        self.assertRegex(bob_list_url, '/lists/list/.+')

        # Mary comes to the home page
        # We use a new browser to make sure none
        # of Bob's info leaks through (cookies etc)
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # no sign of Bob's page
        self.browser.get(self.live_server_url + '/lists/')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Do something cool', page_text)
        self.assertNotIn('Submit the coursework', page_text)

        # Mary starts a new list by entering an item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy bread')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Buy bread')

        # Mary gets their own url
        mary_list_url = self.browser.current_url
        self.assertRegex(mary_list_url, '/lists/list/.+')
        self.assertNotEqual(mary_list_url, bob_list_url)

        # Again, there is no trace of Bob's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Do something cool', page_text)
        self.assertIn('Buy bread', page_text)

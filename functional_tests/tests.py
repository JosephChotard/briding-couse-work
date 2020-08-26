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

    def test_can_a_list_start_and_retrieve_it_later(self):
        # Go visit the site
        self.browser.get(self.live_server_url+'/lists')

        # Notice that it's a To-Do app from the title and the headeer
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

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
        wait_for_row_in_list_table(self, '1. Finish the bridging coursework')

        # There is a text box inviting them to add another item
        # Adds "Submit coursework"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Submit the coursework')
        inputbox.send_keys(Keys.ENTER)

        wait_for_row_in_list_table(self, '1. Finish the bridging coursework')
        wait_for_row_in_list_table(self, '2. Submit the coursework')

        self.fail('Tests aren\'t all implemented')

        # The page updates again to show both items

        # The site has generated a unique url for the use to come back to in thee future

        # On visitting the url the list is still there

        # Satisfied

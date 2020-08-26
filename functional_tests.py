from selenium import webdriver
import unittest
from selenium.webdriver.common import keys
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_a_list_start_and_retrieve_it_later(self):
        # Go visit the site
        self.browser.get('http://localhost:8000/lists')

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
        inputbox.send_keys('Finish the briding coursework')

        # On hitting enter the page updates and the lists '1. Finish the bridging coursework'
        inputbox.send_keys(keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Finish the bridging coursework' for row in rows)
        )

        # There is a text box inviting them to add another item
        # Adds "Submit coursework"
        self.fail('Tests aren\'t all implemented')

        # The page updates again to show both items

        # The site has generated a unique url for the use to come back to in thee future

        # On visitting the url the list is still there

        # Satisfied


if __name__ == '__main__':
    unittest.main(warnings='ignore')

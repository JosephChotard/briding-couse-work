from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_a_list_start_and_retrieve_it_later(self):
        # Go visit the site
        self.browser.get('http://localhost:8000')

        # Notice that it's Joe's website from the title and a To-Do app
        self.assertIn('Joe', self.browser.title)
        self.assertIn('To-Do', self.browser.title)

        self.fail('Tests aren\'t all implemented')
        # They are directly prompted to enter a to-do item

        # Types "Finish the briding coursework" into the text box

        # On hitting enteer the page updates and the page lists 1. Finish the bridging coursework

        # There is a text box inviting them to add another item
        # Adds "Sublit coursework"

        # The page updates again to show both items

        # The site has generated a unique url for the use to come back to in thee future

        # On visitting the url the list is still there

        # Satisfied


if __name__ == '__main__':
    unittest.main(warnings='ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_students_use(self):
        # john goes to the webapp home page
        self.browser.get('http://localhost:8000')

        # the title should have the word Classvotes
        self.assertIn('Classvotes',self.browser.title)
        
        #header text in the home page should have "Vote"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Vote', header_text)

        #There is an input box to enter vote number
        inputbox = self.browser.find_element_by_id('id_vote_number')
        
        #Input box's text has 
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter the vote number'
            )


    def test_teacher_use(self):

        # Jane is the teacher. She visits the site 
        self.browser.get('http://localhost:8000')

        # and finds that there is a hyperlinked text 'Teacher'
        teacher_link=self.browser.find_element_by_class_name('teacher_link')
        self.assertEqual(teacher_link.text,'Teacher')
        
        # she clicks the link
        teacher_link.click()


        # and finds herself in the page with  heading "Create vote"
        teacher_heading=self.browser.find_element_by_class_name('heading')

        # the title should have the word Classvotes
        self.assertIn(teacher_heading.text,'Create Vote')
        # shes finds a input box with id id_vote_number and placeholder "Enter the vote number"

        new_vote_box=self.browser.find_element_by_id('id_vote_number')
        # how to test if an element is an input box. self.assertEqual(new_vote_box.elementType,"Input")
        self.assertEqual(new_vote_box.get_attribute('placeholder'),'Enter the vote number')

        #she enters the number 1 and press enter

        new_vote_box.send_keys('my test 1')
        new_vote_box.send_keys(Keys.ENTER)

        # now she sees the text 'my test 1' in the response
        teacher_heading=self.browser.find_element_by_class_name('heading')
        self.assertNotIn(teacher_heading.text,'Create Vote')
        
        # the title should have the word Classvotes
        self.assertIn(teacher_heading.text,'my test 1')


        ## she presses enter without entering any text. The page now has an error message saying "Vote name can not be empty"
        #new_vote_box.send_keys(Keys.ENTER)
#
#        #refactor!!
#        new_vote_box=self.browser.find_element_by_id('id_vote_number')
#        # how to test if an element is an input box. self.assertEqual(new_vote_box.elementType,"Input")
#        self.assertEqual(new_vote_box.get_attribute('placeholder'),'Enter the vote number')
#
#
#        vote_name_error=self.browser.find_element_by_css_selector('.has-error')




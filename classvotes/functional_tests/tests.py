from selenium import webdriver
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


        # and finds herself in the page with  title "Create vote"
        self.assertIn('Create vote',self.browser.title)


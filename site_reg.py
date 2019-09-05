from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
	def test_reg_1(self):
		try:
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)

			name = browser.find_element_by_tag_name(".first_block .form-group:nth-child(1) input")
			name.send_keys("Vlad")
	
			surname = browser.find_element_by_tag_name(".first_block .form-group:nth-child(2) input")
			surname.send_keys("Savin")
	
			email = browser.find_element_by_css_selector(".first_block .form-group:nth-child(3) input")
			email.send_keys("savin@gmail.com")
	
			phone = browser.find_element_by_css_selector(".second_block .form-group:nth-child(1) input")
			phone.send_keys("89152223333")
	
			address = browser.find_element_by_css_selector(".second_block .form-group:nth-child(2) input")
			address.send_keys("Moscow")
	
			send_button = browser.find_element_by_class_name("btn")
			send_button.click()
	
			time.sleep(1)

			welcome_text_elt = browser.find_element_by_tag_name("h1")
			welcome_text = welcome_text_elt.text
	
			self.assertEqual (welcome_text, "Congratulations! You have successfully registered!", "FailReg")
	
		finally:
			time.sleep(5)
			browser.quit()
	
if __name__ == "__main__":
	unittest.main()
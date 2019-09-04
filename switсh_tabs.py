import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector(".btn")
	button.click()
	
	new_tab = browser.window_handles[1]
	browser.switch_to.window(new_tab)
	
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	
	inp = browser.find_element_by_css_selector("#answer")
	inp.send_keys(y)

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
	alert = browser.switch_to.alert
	alert_text = alert.text
	
	addToClipBoard = alert_text.split(': ')[-1]
	print(addToClipBoard)
	
finally:

	browser.quit()


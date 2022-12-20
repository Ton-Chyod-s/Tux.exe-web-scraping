from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
browser = webdriver.Chrome(executable_path = "chromedriver.exe",chrome_options=chrome_options)
browser.get('https://www.google.com.br/')

time.sleep(60)
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options
                         )
driver.get("http://localhost")
print(driver.title)
time.sleep(2)
driver.find_element_by_id("About Us").click()
text_storage = driver.find_element_by_id("PID-ab2-pg").text
#print("\n",text_storage)
if len (sys.argv) ==1:
    compare_text = "This is about page. Lorem Ipsum Dipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
else:
    compare_text = sys.argv[1]

if (text_storage in compare_text):
    print("Text matched following text found\n\n",compare_text)
    driver.close()
else:
    print("Matching text  not found failing the build now\n\n")
    driver.close()
    sys.exit(1)

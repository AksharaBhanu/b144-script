from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
def test_script1():
    driver = Remote("http://127.0.0.1:4444", options=Options())
    driver.get("http://www.google.com")
    print(driver.title)
    driver.quit()

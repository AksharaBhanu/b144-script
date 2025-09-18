from selenium.webdriver import Chrome
def test_script1():
    print('hi , GE, this is test script1 with selenium')
    driver=Chrome()
    driver.get("http://www.google.com")
    print(driver.title)
    driver.quit()
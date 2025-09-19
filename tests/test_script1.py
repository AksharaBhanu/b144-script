import os

from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import  allure
#pip install allure-pytest
#pytest --alluredir=allure-results
#allure serve allure-results
#Environment Injector
@allure.title('Script2-Bhanu')
@allure.description("-Attach screenshot to allure report")
def test_script1():
    grid_url = os.getenv('GRID_URL', 'http://localhost:4444')
    print(grid_url)
    with allure.step("Step1:Open Chrome Browser"):  # step name
        driver = Remote(grid_url, options=Options())
    with allure.step("Step2:enter the URl: http://www.google.com"):
        driver.get("http://www.google.com")

    with allure.step("Step3:take screenshot"):
        allure.attach(driver.get_screenshot_as_png(), name='Google Page', attachment_type=allure.attachment_type.PNG)

    with allure.step("Step4:close the browser"):
        driver.quit()



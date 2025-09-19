from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import  allure
#pytest --alluredir=allure-results
@allure.title('Script2-Bhanu')
@allure.description("-Attach screenshot to allure report")
def test_script1():
    with allure.step("Step1:Open Chrome Browser"):  # step name
        driver = Remote("http://127.0.0.1:4444", options=Options())
    with allure.step("Step2:enter the URl: http://www.google.com"):
        driver.get("http://www.google.com")

    with allure.step("Step3:take screenshot"):
        allure.attach(driver.get_screenshot_as_png(), name='Google Page', attachment_type=allure.attachment_type.PNG)

    with allure.step("Step4:close the browser"):
        driver.quit()



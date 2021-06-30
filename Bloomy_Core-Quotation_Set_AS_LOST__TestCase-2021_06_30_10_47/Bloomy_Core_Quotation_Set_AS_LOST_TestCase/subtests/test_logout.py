from selenium.webdriver.common.by import By
from src.testproject.decorator import report_assertion_errors


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: Logout
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:47:57
"""


@report_assertion_errors
def test_main(driver):
    """Logout from the application."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"

    # 1. Click 'T
    # 		           Settings'
    t_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tT\n\t\t           Settings     ']")
    t_settings.click()

    # 2. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 3. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

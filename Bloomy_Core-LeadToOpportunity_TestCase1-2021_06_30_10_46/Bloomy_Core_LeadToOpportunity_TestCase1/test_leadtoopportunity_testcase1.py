from addons.random_data_generator import RandomDataGenerator
from addons.string_utils import StringUtils
from distutils.util import strtobool
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from subtests import test_login
from subtests import test_logout
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: LeadToOpportunity_TestCase1
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:46:32
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="LeadToOpportunity_TestCase1")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1. Go to the lead doctype.(Desk>> CRM>>Lead) or Type \"Lead in search bar\"\".

    2. Open Lead.3. Click on create Button in top right corner and select Opportunity.  It will redirect you to on Opportunity doctype.5. Save.
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ExpectedLeadNm = ""
    ActualLeadName = ""
    ExpectedLeadID = ""
    ActualLeadIDonOpportunityDoc = ""
    username = ""
    pwd = ""
    ExpectedMobileNo = ""
    ActualMobileNoOnOpportunityDoc = ""
    RandomLeadName = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login to the Application
    test_login.test_main(driver)

    # 3. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 4. Type 'lead l' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("lead l")

    # 5. Click 'Lead List'
    lead_list = driver.find_element(By.XPATH,
                                    "//li[. = 'Lead List']")
    lead_list.click()

    # 6. Does 'Lead7' contain 'Lead'?
    lead7 = driver.find_element(By.XPATH,
                                "//div[. = 'Lead']")
    step_output = lead7.text
    assert step_output and ("Lead" in step_output)

    # 7. Click 'New4'
    new4 = driver.find_element(By.XPATH,
                               "//button[. = 'New']")
    new4.click()

    # 8. Is 'New Lead 11' visible?
    new_lead_11 = driver.find_element(By.XPATH,
                                      "//div[. = 'New Lead 1']")
    assert new_lead_11.is_displayed()

    # 9. Does 'Not Saved' contain 'Not Saved'?
    not_saved = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Not Saved']")
    step_output = not_saved.text
    assert step_output and ("Not Saved" in step_output)

    # 10. Click 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[1]/form/div[2]//input")
    input64.click()

    # 11. Generate random name
    step_output = driver.addons().execute(
        RandomDataGenerator.generatename(
        ))
    RandomLeadName = step_output

    # 12. Type '{RandomLeadName}' in 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[1]/form/div[2]//input")
    input64.send_keys(f'{RandomLeadName}')

    # 13. Get text from 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[1]/form/div[2]//input")
    step_output = input64.get_attribute("value")
    ExpectedLeadNm = step_output

    # 14. Click 'INPUT67'
    input67 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[1]//input")
    input67.click()

    # 15. Type 'Add Title' in 'INPUT67'
    input67 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[1]//input")
    input67.send_keys("Add Title")

    # 16. Click 'INPUT68'
    input68 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[2]//input")
    input68.click()

    # 17. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 18. Type 'Add1' in 'INPUT68'
    input68 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[2]//input")
    input68.send_keys("Add1")

    # 19. Click 'INPUT69'
    input69 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[3]//input")
    input69.click()

    # 20. Click 'INPUT69'
    input69 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[3]//input")
    input69.click()

    # 21. Type 'Add2' in 'INPUT69'
    input69 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[3]//input")
    input69.send_keys("Add2")

    # 22. Click 'INPUT70'
    input70 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[4]//input")
    input70.click()

    # 23. Type 'mumbai' in 'INPUT70'
    input70 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[4]//input")
    input70.send_keys("mumbai")

    # 24. Click 'INPUT71'
    input71 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[5]//input")
    input71.click()

    # 25. Type 'india' in 'INPUT71'
    input71 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[5]//input")
    input71.send_keys("india")

    # 26. Click 'INPUT72'
    input72 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[1]//input")
    input72.click()

    # 27. Type 'maharastra' in 'INPUT72'
    input72 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[1]//input")
    input72.send_keys("maharastra")

    # 28. Click 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[2]//input")
    input73.click()

    # 29. Clear 'clearcon' contents
    clearcon = driver.find_element(By.XPATH,
                                   "//div[7]/div[2]/div[2]/form/div[2]//input")
    clearcon.clear()

    # 30. Type 'india' in 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[2]//input")
    input73.send_keys("india")

    # 31. Click 'India'
    india = driver.find_element(By.XPATH,
                                "//li[. = 'India']")
    india.click()

    # 32. Click 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[3]/div/div[2]/div/input")
    input74.click()

    # 33. Type '40066' in 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[3]/div/div[2]/div/input")
    input74.send_keys("40066")

    # 34. Click 'INPUT75'
    input75 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[1]//input")
    input75.click()

    # 35. Type '6666666666' in 'INPUT75'
    input75 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[1]//input")
    input75.send_keys("6666666666")

    # 36. Click 'INPUT76'
    input76 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[2]//input")
    input76.click()

    # 37. Type '8888888888' in 'INPUT76'
    input76 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[2]//input")
    input76.send_keys("8888888888")

    # 38. Get text from 'getmobileno'
    getmobileno = driver.find_element(By.XPATH,
                                      "//div[8]/div[2]/div/form/div[2]//input")
    step_output = getmobileno.get_attribute("value")
    ExpectedMobileNo = step_output

    # 39. Click 'INPUT77'
    input77 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[3]//input")
    input77.click()

    # 40. Type '4447' in 'INPUT77'
    input77 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[3]//input")
    input77.send_keys("4447")

    # 41. Click 'savebu'
    savebu = driver.find_element(By.XPATH,
                                 "//button[. = 'Save']")
    savebu.click()

    '''
    # (STEP DISABLED)
    # 42. Click 'clicksa'
    clicksa = driver.find_element(By.XPATH,
    "//button[. = 'Save']")
    clicksa.click()
    '''

    # 43. Get text from 'Pers'
    pers = driver.find_element(By.XPATH,
                               "//h1//div[. = 'Pers']")
    step_output = pers.get_attribute("value")
    ActualLeadName = step_output

    # 44. Does 'Lead8' contain 'Lead'?
    lead8 = driver.find_element(By.XPATH,
                                "//span/span[. = 'Lead']")
    step_output = lead8.text
    assert step_output and ("Lead" in step_output)

    # 45. Get text from 'CRM-LEAD-2021-00371'
    crm_lead_2021_00371 = driver.find_element(By.XPATH,
                                              "//h6[. = 'CRM-LEAD-2021-00371']")
    step_output = crm_lead_2021_00371.get_attribute("value")
    ExpectedLeadID = step_output

    # 46. Click 'Create'
    create = driver.find_element(By.XPATH,
                                 "//button[. = '\t\t\t\tCreate ']")
    create.click()

    # 47. Click 'Opportunity2'
    opportunity2 = driver.find_element(By.XPATH,
                                       "//div[2]/div[1]/div[1]//a[. = 'Opportunity']")
    opportunity2.click()

    # 48. Click 'INPUT97'
    input97 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input97.click()

    # 49. Get text from 'INPUT97'
    input97 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    step_output = input97.get_attribute("value")
    ActualLeadIDonOpportunityDoc = step_output

    # 50. Is 'New Opportunity 1' visible?
    new_opportunity_1 = driver.find_element(By.XPATH,
                                            "//div[. = 'New Opportunity 1']")
    assert new_opportunity_1.is_displayed()

    # 51. Does 'Open' contain 'Open'?
    open = driver.find_element(By.XPATH,
                               "//span/span[. = 'Open']")
    step_output = open.text
    assert step_output and ("Open" in step_output)

    # 52. Click 'INPUT98'
    input98 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div[2]/form/div[1]//input")
    input98.click()

    # 53. Type 'vap' in 'INPUT98'
    input98 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div[2]/form/div[1]//input")
    input98.send_keys("vap")

    # 54. Click 'VapeCo9'
    vapeco9 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco9.click()

    # 55. Click 'SPAN12'
    span12 = driver.find_element(By.XPATH,
                                 "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[7]/div/span")
    span12.click()

    # 56. Click '6666666666'
    _6666666666 = driver.find_element(By.XPATH,
                                      "//div[4]//div[. = '6666666666']")
    _6666666666.click()

    # 57. Get text from 'getmobile'
    getmobile = driver.find_element(By.XPATH,
                                    "//div[7]/div[2]/div[2]/form/div[4]/div/div/div[2]")
    step_output = getmobile.get_attribute("value")
    ActualMobileNoOnOpportunityDoc = step_output

    # 58. Does 'Not Saved1' contain 'Not Saved'?
    not_saved1 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Not Saved']")
    step_output = not_saved1.text
    assert step_output and ("Not Saved" in step_output)

    # 59. Compares '{ExpectedLeadNm}' with '{ActualLeadName}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadNm}',
            secondString=f'{ActualLeadName}',
            ignoreCase=False,
            expectedResult=0))

    # 60. Compares '{ExpectedLeadID}' with '{ActualLeadIDonOpportunityDoc}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadID}',
            secondString=f'{ActualLeadIDonOpportunityDoc}',
            ignoreCase=False,
            expectedResult=0))

    # 61. Compares '{ExpectedMobileNo}' with '{ActualMobileNoOnOpportunityDoc}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedMobileNo}',
            secondString=f'{ActualMobileNoOnOpportunityDoc}',
            ignoreCase=False,
            expectedResult=0))

    # 62. Click 'Save19'
    save19 = driver.find_element(By.XPATH,
                                 "//div[4]//button[. = 'Save']")
    save19.click()

    # 63. Does 'Open' contain 'Open'?
    open = driver.find_element(By.XPATH,
                               "//span/span[. = 'Open']")
    step_output = open.text
    assert step_output and ("Open" in step_output)

    # 64. Logout from the application
    test_logout.test_main(driver)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from helium import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

username = "username"
password = "password"

default_options = [
    "--disable-extensions",
    "--disable-user-media-security=true",
    "--allow-file-access-from-files",
    "--use-fake-device-for-media-stream",
    "--use-fake-ui-for-media-stream",
    "--disable-popup-blocking",
    "--disable-infobars",
    "--enable-usermedia-screen-capturing",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--auto-select-desktop-capture-source=Screen 1",
    "--disable-blink-features=AutomationControlled",
    "--disable-notifications"
]

headless_options = [
    "--headless",
    "--use-system-clipboard",
    "--window-size=1920x1080"
]

def browser_options(chrome_type):
    webdriver_options = webdriver.ChromeOptions()
    notification_opt = {"profile.default_content_setting_values.notifications": 1}
    webdriver_options.add_experimental_option("prefs", notification_opt)
    if chrome_type == "headless":
        var = default_options + headless_options
    else:
        var = default_options
    for d_o in var:
        webdriver_options.add_argument(d_o)
    return webdriver_options

def get_webdriver_instance(browser=None):
    base_url = "https://accounts.teachmint.com/"
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"

    driver = Chrome(service=ChromeService(ChromeDriverManager().install()),
                    options=browser_options(browser))
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_com,mand')
    driver.maximize_window()
    driver.get(base_url)
    set_driver(driver)
    return driver

def enter_phone_number_otp(driver, creds):
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(creds[0])
    time.sleep(1)
    print("entered user phone number {}".format(creds[0]))
    driver.find_element(By.ID, "send-otp-btn-id").click()
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.CSS_SELECTOR, "loader")))
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.CLASS_NAME, "loader")))
    time.sleep(1)
    _input_otp_field = "//input[@data-group-idx='{}']"
    for i, otp in enumerate(creds[1]):
        otp_field = _input_otp_field.format(str(i))
        write(otp, into=S(otp_field))
    print("entered otp {}".format(creds[1]))
    time.sleep(1)
    driver.find_element(By.ID, "submit-otp-btn-id").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='main']/div[4]/div[1]/div/div[1]").click()
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.CSS_SELECTOR, "loader")))
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.CLASS_NAME, "loader")))
    time.sleep(1)
    print("successfully entered user phone number and otp")


def generate_school_leaving(driver):

    driver.refresh()
    main_window_handle = driver.current_window_handle
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[1]/div/div/div[1]/div[7]/div/div/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[1]/div/div/div[1]/div[7]/div/div[2]/div/a[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div").click()
    time.sleep(9)
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/div[3]/div[3]/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div[2]/button[2]/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div/div/div/div/div[3]/div[1]/div/table/tbody/tr/td[1]/label/div[1]").click()
    time.sleep(5)
    # Optionally, you can wait for the modal to fully load before interacting with it

    # Perform click action on the modal div
    driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div/div/div/div/div[3]/div[1]/div/table/tbody/tr/td[4]/button/div").click()
    time.sleep(8)
    driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div/div/div/footer/div/button").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//*[@id='download']").click()
    time.sleep(5)
    driver.switch_to.window(main_window_handle)
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[1]/div/div/div[1]/div[7]/div/div/div").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[1]/div/div/div[1]/div[7]/div/div/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/div[3]/div[3]/div[1]/div/div/div[1]/div[7]/div/div[2]/div/a[1]").click()
    time.sleep(5)
    if(driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div/div/div/div/div/div[6]/div[1]/div/table/tbody/tr[1]/td[1]/div/div[2]/p[1]").text=="Sam" and driver.find_element(By.XPATH,"//*[contains(text(), 'Study Certificate')]").text=="Study Certificate"):
        print("Succesfully Validated")
    else:
        print("Not Succesfully Validated")












def login(admin_credentials=["0000020232", "120992", "@Automation-2"], account_name="@Automation-2"):
    driver = get_webdriver_instance()
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.CSS_SELECTOR, "loader")))
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.CLASS_NAME, "loader")))
    time.sleep(1)
    enter_phone_number_otp(driver, admin_credentials)
    user_name = "//div[@class='profile-user-name']/..//div[text()='" + account_name + "']"
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, user_name)))
    # driver.find_element(By.XPATH, user_name).click()
    # dashboard_xpath = "//a[text()='Dashboard']"
    # WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, dashboard_xpath)))
    time.sleep(5)
    # refresh()
    generate_school_leaving(driver)
    return driver

def main():
    driver = login()
    driver.quit()

if __name__ == "__main__":
    print("start")
    main()
    print("end")

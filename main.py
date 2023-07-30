from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service("/Users/valerybichkov/Desktop/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=service)

TCB_USERNAME = ""
TCB_PASSWORD = ""

LnkDin_USERNAME = ""
LnkDin_PASSWORD = ""
class LoginToTcb:
    curpage = ""
    def login_step_1(self):
        driver.get("https://login.tcb.ac.il/nidp/saml2/sso?id=tcbloa2&sid=0&option=credential&sid=0")
        time.sleep(5)

        username = driver.find_element(By.ID, "Ecom_User_ID")
        username.send_keys(TCB_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(5)


    def login_step_2(self):
        time.sleep(5)
        userpassword = driver.find_element(By.ID, "ldapPasswordCardClick")
        userpassword.click()
        time.sleep(5)

    def login_step_3(self):
        time.sleep(5)
        userpassword = driver.find_element(By.ID, "ldapPassword")
        userpassword.send_keys(TCB_PASSWORD)
        userpassword.send_keys(Keys.ENTER)
        time.sleep(5)


#tcb = LoginToTcb()
#tcb.login_step_1()
#tcb.login_step_2()
#tcb.login_step_3()


class LinkdInJobs:
    def login_linkedin(self):
        driver.get("https://linkedin.com/checkpoint/lg/sign-in-another-account")
        time.sleep(5)
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("")
        password.send_keys("")
        password.send_keys(Keys.ENTER)

        time.sleep(3)

        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3662733631&keywords=full%20stack%20developer&refresh=true")
        time.sleep(10)

        jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-list a")
        for n in range(len(jobs)):
            print(jobs[n].text)
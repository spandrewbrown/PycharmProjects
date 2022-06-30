import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Gmail:
    global usernameXPath, passwordXPath, NextXPath, Pause, SearchXPath, AllowButtonXPath
    usernameXPath = '//*[@type="email"]'
    passwordXPath = '//*[@type="password"]'
    NextXPath = '//button[@type="button"]//span[text()="Next"]'
    Pause = 10
    SearchXPath = '(//*[@aria-label="Search all conversations"])[1]'
    AllowButtonXPath = '//span[text()="Allow"]'

    def __init__(self, driver):
        self.driver = driver

    def Username(self, username):
        WebDriverWait(self.driver, Pause).until(EC.presence_of_element_located((By.XPATH, usernameXPath))
                                                ).send_keys(username)

    def Password(self, password):
        WebDriverWait(self.driver, Pause).until(EC.presence_of_element_located((By.XPATH, passwordXPath))
                                                ).send_keys(password)

    def NextButton(self):
        self.driver.find_element_by_xpath(NextXPath).click()

    def LoginToGmail(self, username, password):
        self.Username(username)
        time.sleep(1)
        self.NextButton()
        time.sleep(2)
        self.Password(password)
        self.NextButton()

    def SearchForMessage(self, messageString, num):
        WebDriverWait(self.driver, Pause).until(EC.presence_of_element_located((By.XPATH, SearchXPath))
                                                ).send_keys(messageString)
        time.sleep(3)
        i = 0
        for i in range(num):
            WebDriverWait(self.driver, Pause).until(EC.presence_of_element_located((By.XPATH, SearchXPath))
                                                    ).send_keys(Keys.DOWN)
        WebDriverWait(self.driver, Pause).until(EC.presence_of_element_located((By.XPATH, SearchXPath))
                                                ).send_keys(Keys.RETURN)

    def AllowSISAccess(self):
        WebDriverWait(self.driver, Pause).until(EC.presence_of_element_located((By.XPATH, AllowButtonXPath))).click()


import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from myconstants import categoryConstants as lc
import tests.LoginTests.test_successfull_login as login
from time import sleep

class TestMycertificatewiewdowland():
  def setup_method(self):
    test_successfull_login = login.Testsuccessfulllogin()
    test_successfull_login.setup_method(self)
    test_successfull_login.test_successfulllogin()
    #self.driver =test_successfull_login.getDriver()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_mycertificatewiewdowland(self):
    sleep(5)
    self.driver.get("https://www.btkakademi.gov.tr/portal")
    profile_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,lc.PROFILE_BUTTON_XPATH)))
    profile_button.click()

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

from time import sleep
from myconstants import loginConstants as lc
from myconstants import credentials_constants as cc

class Testsuccessfulllogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get(lc.BASE_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_successfulllogin(self):
    login_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,lc.LOGIN_BUTTON_XPATH)))
    login_button.click()
    edevlet_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,lc.EDEVLET_BUTTON_XPATH)))
    edevlet_button.click()
    tcno_textbox=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,lc.TCNO_TEXTBOX_XPATH)))
    tcno_textbox.click()
    tcno_textbox.send_keys(cc.USER_TCNO)
    password_textbox=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,lc.PASSWORD_TEXTBOX_XPATH)))
    password_textbox.click()
    password_textbox.send_keys(cc.USER_PASSWORD)
    glogin_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,lc.GLOGIN_BUTTON_XPATH)))
    glogin_button.click()
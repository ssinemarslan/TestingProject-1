#Test Senaryosu  Adı: Kurs Detaylarını İçeriğinin Eğitmeninin Görüntüleme Kontrolü
#Test Case1:Kurs Detayları Görüntüleme Kontrolü
# Generated by Selenium IDE
#alt menü nedense basmıyooo.
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

from myconstants import categoryConstants as cco
from time import sleep

class TestDetailscourse():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get(cco.PORTAL_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_detailscourse(self):
    # self.driver.get("https://www.btkakademi.gov.tr/portal")
    # self.driver.set_window_size(1382, 744)
    software_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,cco.SOFTWARE_WORLD_BUTTON_XPATH)))
    software_button.click()
    under_button=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,cco.UNDER_BUTTON_XPATH)))
    under_button.click()
    testingsoftware_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,cco.TESTING_SOFTWARE_BUTTON_XPATH)))
    testingsoftware_button.click()
    testingsoftware_education=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,cco.TESTING_SOFTWARE_EDUCATION_XPATH)))
    testingsoftware_education.click()
    
  

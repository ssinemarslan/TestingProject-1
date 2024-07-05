#Test Senaryosu: Arama Textboxı Kullanılarak Eğitim Araması Kontrolü
#Test Case3: Boşluk Tuşu Kullanılarak Arama Yapılarak Kursların Listelenmesi Kontrolü
#test fail.
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

class Testwithoutdataentry():
  def setup_method(self, method):
     self.driver = webdriver.Chrome()
     self.driver.get(cco.PORTAL_URL)
     self.driver.maximize_window()
     self.vars = {}
  
  def teardown_method(self, method):
     self.driver.quit()
  
  def test_failedsearchingtextbox(self):
     searchingtextbox=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,cco.SEARCHING_TEXTBOX_NAME)))
     searchingtextbox.click()
     searchingtextbox.send_keys(" ")
     searchingbutton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,cco.SEARCHING_BUTTON_XPATH)))
     searchingbutton.click()
     searching_result=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,cco.SEARCHING_RESULT_XPATH)))
     assert searching_result.text=="Belirtilen kriterlere uygun eğitim bulunamamıştır.Yeniden arama yapınız..."
    
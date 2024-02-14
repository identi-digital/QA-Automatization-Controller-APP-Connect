from typing import List, Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

time_timeout = 30

class Navigator(webdriver.Remote, By):

    def __init__(self, command_executor="http://127.0.0.1:4444", keep_alive=True, file_detector=None, options: BaseOptions | List[BaseOptions] = None) -> None:
        super().__init__(command_executor, keep_alive, file_detector, options)

    def select_element_by_XPATH(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.XPATH, location)))
        self.element = self.find_element(by=self.XPATH, 
        value=location)

    def select_element_by_CssSelector(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.CSS_SELECTOR, location))) 
        self.element = self.find_element(by=self.CSS_SELECTOR, 
        value=location)

    def select_element_by_ID(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.ID, location)))
        self.element = self.find_element(by=self.ID, value=location)

    def select_element_by_ClassName(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.CLASS_NAME, location)))
        self.element = self.find_element(by=self.CLASS_NAME, value=location)

    def select_element_by_text(self, location: str):
        
        loc = f'//*[contains(text(), "{location}")]'

        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.XPATH, loc)))
        self.element = self.find_element(by=self.XPATH, value=loc)

    def filter_selector(self, type_location:str, location:str):
        match type_location:
            case 'css':
                self.select_element_by_CssSelector(location)
            case 'xpath':
                self.select_element_by_XPATH(location)
            case 'classname':
                self.select_element_by_ClassName(location)
            case 'id':
                self.select_element_by_ID(location)
            case 'text':
                self.select_element_by_text(location)

    # def time_to_wait(seconds:int):

    #     time.sleep(3)

    def init_session(self, target_URL:str):
        
        self.get(target_URL)
        self.set_window_size(1500,1000)

    def type_element(self, content:str, location:str, type_location:str):

        self.filter_selector(type_location, location)
        self.element.send_keys(content)

    def click_element(self, location:str, type_location:str):
        self.filter_selector(type_location, location)
        self.element.click()

    def edit_style_element(self, type_location, location, prop, value):

        self.filter_selector(type_location=type_location, location=location)

        script = f"arguments[0].style.{prop} = '{value}';"

        self.execute_script(script, self.element)
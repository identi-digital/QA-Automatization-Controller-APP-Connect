from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

time_timeout = 10
habilitated_keyboard = False

import time

class NavigatorAppium(webdriver.Remote, AppiumBy):

    def select_element_by_ClassName(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.CLASS_NAME, location)))
        self.element = self.find_element(by=self.CLASS_NAME, value=location)

    def select_element_by_ID(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.ACCESSIBILITY_ID, location)))
        self.element = self.find_element(by=self.ACCESSIBILITY_ID, value=location)

    def select_element_by_XPATH(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.XPATH, location)))
        self.element = self.find_element(by=self.XPATH, 
        value=location)

    def select_element_by_CssSelector(self, location:str):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.CSS_SELECTOR, location))) 
        self.element = self.find_element(by=self.CSS_SELECTOR, 
        value=location)

    def select_element_by_UIAUTOMATOR_TEXT(self, location:str):

        value = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{location}"))'

        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.ANDROID_UIAUTOMATOR, value)))

        self.element = self.find_element(by=self.ANDROID_UIAUTOMATOR, value=value)

    def select_element_by_UIAUTOMATOR_DESC(self, location:str):

        value = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().descriptionStartsWith("{location}"))'

        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.ANDROID_UIAUTOMATOR, value)))

        self.element = self.find_element(by=self.ANDROID_UIAUTOMATOR, value=value)

    def select_multiple_elements_by_XPATH(self,  location):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_all_elements_located((self.XPATH, location)))

        self.elements=self.find_elements(by=self.XPATH, value=location)

    def select_child_elements_by_XPATH(self,  location):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.XPATH, location)))

        parent=self.find_element(by=self.XPATH, value=location)

        self.elements = parent.find_elements(by=self.XPATH, value="*")


    def select_child_elements_by_ID(self, location):
        WebDriverWait(driver=self, timeout=time_timeout).until(EC.presence_of_element_located((self.ACCESSIBILITY_ID, location)))

        parent=self.find_element(by=self.ACCESSIBILITY_ID, value=location)

        self.elements = parent.find_elements(by=self.XPATH, value="*")

    def recursivity_child_elements(self, index:int):

        self.elements = self.elements[index].find_elements(by=self.XPATH, value="*")



    def filter_selector(self, typeLocation:str, location:str):
        match typeLocation:
            case 'css':
                self.select_element_by_CssSelector(location)
            case 'xpath':
                self.select_element_by_XPATH(location)
            case 'id':
                self.select_element_by_ID(location)
            case 'classname':
                self.select_element_by_ClassName(location)
            case 'ui-text':
                self.select_element_by_UIAUTOMATOR_TEXT(location)
            case 'ui-desc':
                self.select_element_by_UIAUTOMATOR_DESC(location)

    def type_element(self, content:str, location:str, type_location:str):

        self.click_element(location, type_location)
        self.filter_selector(type_location, location)
        self.element.send_keys(content)
        
        if habilitated_keyboard:
            self.hide_keyboard()

    def click_element(self, location:str, type_location:str):
        self.filter_selector(type_location, location)
        self.element.click()

    def movement_in_view(self, percentage:int):

        size = self.get_window_size()

        width = size["width"]
        height = size["height"]

        center_x = width/2
        center_y = height/2

        final_y = center_y - (height/100*percentage)
        actions = ActionChains(self)
        actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(center_x, center_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(center_x, final_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def click_by_coordinates(self, axis_x, axis_y):
        
        actions = ActionChains(self)
        actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(axis_x, axis_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()


    def click_from_multiple(self, index:int):

        self.element = self.elements[index]
        self.element.click()

    def type_from_multiple(self, index:int, content):

        self.element = self.elements[index]
        self.element.click()
        self.element.send_keys(content)

        if habilitated_keyboard:
            self.hide_keyboard()

        time.sleep(1)

    # def change_location(self, long, lat):

    #     self.set_location()
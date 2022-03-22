# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:02:30 2021

@author: bbalushev
"""

import time
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pydoc import locate


class Web(object):
    __TIMEOUT = 15
    resource_name_for_locators = ''

    # ================================ Initialization method ================================
    def __init__(self, web_driver) -> None:
        """ Constructor method

            Method parameters:
               web_driver -> contains driver object which will interact with our web browser

            Return value -> None

        """

        super(Web, self).__init__()
        self._web_driver_wait = WebDriverWait(web_driver, self.__TIMEOUT)
        self._web_driver = web_driver

    # ============================== Save driver version method ==============================
    def save_driver_version(self, browser: str = 'chrome') -> None:
        """ save_driver_version method driver version in to the text file

            Method parameters:
                browser -> contains the name of the browser

            Return value -> None

        """
        if browser.lower() == 'chrome':
            version = self._web_driver.capabilities['chrome']['chromedriverVersion'].split('.')[0]
            with open("drivers/drivers version/chromedriver_version.txt", "w") as text_file:
                text_file.write(version)
        elif browser.lower() == 'firefox':
            pass
        else:
            pass

    # ================================ Navigate to url method ================================
    def window_maximize(self) -> None:
        """ window_maximize method open set web browser in full screen mode

            Method parameters -> None
            Return value -> None

        """

        self._web_driver.maximize_window()

    # ================================ Navigate to url method ================================
    def open_url(self, url: str) -> None:
        """ open_url method open the url in to the web browser

            Method parameters:
                url -> contains the url string

            Return value -> None

        """
        if url not in (None, ''):
            self._web_driver.get(url)
        else:
            raise Exception("Can't open empty url")

    # ================================= Navigate to url method =================================
    def navigate_to_url(self, url: str) -> None:
        """ navigate_to_url method open the url in to the web browser

           Method parameters:
               url -> contains the url string

           Return value -> None

       """

        self.open_url(url)

    # ================================ Close web browser method ================================
    def close_browser(self) -> None:
        """ close_browser method close the web browser which is in focus

            Method parameters -> None
            Return value -> None

        """

        self._web_driver.close()

    # ================================ Web browser quit method ================================
    def quit_browser(self) -> None:
        """ quit_browser method closes all the browsers

            Method parameters -> None
            Return value -> None

        """

        self._web_driver.quit()

    # ================================ Execute js script method ================================
    def execute_script(self, script: str) -> None:
        """ execute_script method execute js script

            Method parameters:
                script -> contains js script which must be executed

            Return value -> None

        """

        self._web_driver.execute_script(script)

    # ================================ Find single element method ================================
    def find_element(self, locator: str, vendor: str = '', list_index: int = 0, method: str = 'CSS'):
        """ find_element method finds element represented in our DOM

            Method parameters:
                locator -> contains the name of the locator
                vendor -> contains the name of the vendor
                list_index -> contains index when we fetch list element
                method -> contains the method which will be used

            Return value -> the found element

        """

        if vendor != '':
            element = locate('source.web_source.locators.%s.%s' % (vendor, locator))
        else:
            element = locate('source.web_source.locators.%s.%s' % (self.resource_name_for_locators, locator))

        if type(element) == tuple:
            element = element[list_index]
        else:
            element = element.replace('@index@', str(list_index))

        if element is not None:
            if method.lower() == 'xpath':
                return self._web_driver_wait.until(EC.presence_of_element_located((By.XPATH, element)),
                                                   message=f"Element '{locator}' with XPATH '{str(element)}' "
                                                           f"was not found!")
            else:
                return self._web_driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)),
                                                   message=f"Element '{locator}' with CSS '{str(element)}' "
                                                           f"was not found!")
        else:
            raise Exception(f'Locator with "{element}" name not found !!!')

    # ================================ Web element click method ================================
    def click_on_element(self, locator: str, vendor: str = '', list_index: int = 0, method: str = 'CSS') -> None:
        """ click_on_element method find the element and click over it

            Method parameters:
               locator -> contains the name of the locator
               vendor -> contains the name of the vendor
               list_index -> contains index when we fetch list element
               method -> contains the method which will be used

            Return value -> None

        """

        iteration = 0
        for _ in range(5):
            try:
                self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method).click()
                break
            except Exception as e:
                print(e)
                time.sleep(2)
                iteration += 1
                continue

        if iteration == 5:
            raise Exception(f"Can't click on {locator}")

    # ============================= Web element click with JS method =============================
    def click_on_element_with_js(self, locator: str, vendor: str = '', list_index: int = 0, method: str = 'CSS') -> None:
        """ click_on_element_with_js method find the element and click over it using js script

            Method parameters:
               locator -> contains the name of the locator
               vendor -> contains the name of the vendor

            Return value -> None

        """

        print(f"===> Clicking {locator} with javascript")
        element = self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method)
        code = "document.querySelector('%s').click()" % element
        self.execute_script(code)

    # =========================== Verify element is not present method ===========================
    def verify_element_not_present(self, locator: str, vendor: str = '', timeout: int = 15) -> None:
        """ verify_element_not_present method verify the element is not present

           Method parameters:
              locator -> contains the name of the locator
              vendor -> contains the name of the vendor
              timeout -> contains timeout value in seconds

           Return value -> None

       """

        time.sleep(0.05)
        web_driver_wait = WebDriverWait(self._web_driver, timeout)

        if vendor != '':
            element = locate('source.web_source.locators.%s.%s' % (vendor, locator))
        else:
            element = locate('source.web_source.locators.%s.%s' % (self.resource_name_for_locators, locator))

        web_driver_wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, element)),
                              message="Element '" + locator + "' is still present!")

    # ============================ Verify element text ============================
    def verify_element_text(self,
                            locator: str,
                            vendor: str = '',
                            list_index: int = 0,
                            method: str = 'CSS',
                            text: str = '',
                            contains_in_text: bool = False) -> None:
        """ verify_element_text method verify the element is not present

            Method parameters:
              locator -> contains the name of the locator
               vendor -> contains the name of the vendor
               method -> contains the method which will be used
               text -> contains the text which must be compared

            Return value -> None

        """

        element_text = self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method).text
        if contains_in_text:
            assert text in element_text, (f'Text: "{element_text}" does not contain "{text}"')
        else:
            assert element_text == text, (f'Element text is: "{element_text}" while it should be: "text"')

    # ============================ Get element attribute value method ============================
    def get_element_attribute(self,
                              locator: str,
                              vendor: str = '',
                              list_index: int = 0,
                              method: str = 'CSS',
                              attribute: str = 'value') -> str:
        """ get_element_attribute method get the attribute value from the located element

            Method parameters:
               locator -> contains the name of the locator
               vendor -> contains the name of the vendor
               method -> contains the method which will be used
               attribute -> contains the name of the attribute

            Return value -> attribute value

        """

        return self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method).get_attribute(attribute)

    # ======================= Verify text is present on the web page method =======================
    def verify_text_present_on_page(self, text: str) -> None:
        """ get_element_attribute method verify the text is present on the current web page

            Method parameters:
              text - > contains the text to be verified

            Return value -> None

        """

        assert str(text) in self._web_driver.page_source, ("Text '" + text + "' is not present!")

    # ======================= Verify element is present on the web page =======================
    def verify_element_present(self, locator: str, vendor: str = '', timeout=15, method='CSS') -> None:
        """ get_element_attribute method verify the text is present on the current web page

            Method parameters:
              locator -> contains the name of locator
              vendor -> contains vendor name
              timeout -> contains time to wait in sek.
              method -> contains method used for location of element

            Return value -> None

        """

        web_driver_wait = WebDriverWait(self._web_driver, timeout)

        if vendor != '':
            element = locate('source.web_source.locators.%s.%s' % (vendor, locator))
        else:
            element = locate('source.web_source.locators.%s.%s' % (self.resource_name_for_locators, locator))

        if element is not None:
            if method == 'Xpath':
                web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, element)),
                                      message=f"Element '{locator}' with XPATH: '{str(element)}' is not present!")
            else:
                web_driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)),
                                      message=f"Element '{locator}' with CSS: '{str(element)}' is not present!")

        else:
            raise Exception(f'Locator with "{element}" name not found !!!')

    # ============================ Take screenshot and save it method ============================
    def take_screenshot(self, file_name: str, file_extension: str, formatter: str) -> object:
        """ take_screenshot method take a screenshot and save it like
            file_mame + _ + current datetime + . +  file_extension

            Method parameters:
              file_name - > contains the name of the saved file
              file_extension -> contains the extension of the saved file
              formatter -> contains formatter settings

            Return value -> Screenshot file

        """

        if formatter == 'pretty':
            dtm = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            file_path = 'screenshots/%s-%s.%s' % (file_name, dtm, file_extension)

            self._web_driver.get_screenshot_as_file(file_path)

        return self._web_driver.get_screenshot_as_png()

    # ================================= Scroll to element method =================================
    def scroll_to_element(self, locator: str, vendor: str = '', list_index: int = 0, method: str = 'CSS') -> None:
        """ scroll_to_element method scrolled to the specific item on the current webpage

            Method parameters:
               vendor -> contains the name of the vendor
               locator -> contains the name of the locator
               method -> contains the method which will be used

            Return value -> None

        """

        print('===> Scrolling to element: ' + locator)
        element = self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method)
        actions = ActionChains(self._web_driver)
        actions.move_to_element(element).perform()

    # ========================= Enter text without verification method =========================
    def fill_field_without_verification(self,
                                        locator: str,
                                        vendor: str = '',
                                        list_index: int = 0,
                                        text: str = '',
                                        method='CSS') -> None:
        """ fill_field_without_verification method enter text without verification

            Method parameters:
              vendor -> contains the name of the vendor
              locator -> contains the name of the locator
              text -> contains text to be entered
              method -> contains the method which will be used

            Return value -> None

        """
        print(f"===> Entering text: {text} in: {locator}")
        self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method).send_keys(text)

    # ==================================== Fill field method ====================================
    def fill_field(self,
                   locator: str,
                   vendor: str = '',
                   list_index: int = 0,
                   text: str = '',
                   encrypted: bool = False,
                   method: str = 'CSS',
                   with_click: bool = False,
                   press_enter: bool = False) -> None:
        """ fill_field method gives us an opportunity to enter normal or encrypted text,
            we can choose after entering text to press enter or not

            Method parameters:
              locator -> contains the name of the locator
              vendor -> contains the name of the vendor
              list_index -> contains the number of element in the list
              text -> contains text to be entered
              encrypted -> encrypted text flag
              method -> contains the method which will be used
              with_click -> click on element flag
              press_enter -> press enter flag

            Return value -> None

        """

        if with_click:
            self.click_on_element(locator=locator)

        entered_text = text
        filling_field_success = False

        if encrypted:
            from common_functions.crypto import Crypto
            crypto = Crypto()
            entered_text = crypto.decrypt(text)

        if entered_text is None:
            raise Exception('Trying to populate field with None!')
        else:
            element = self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method)

            for _ in range(2):
                element.send_keys(Keys.CONTROL, 'a')
                element.send_keys(Keys.BACK_SPACE, entered_text)
                time.sleep(1)
                if element.get_attribute('value') == entered_text:
                    filling_field_success = True
                    break

            if not filling_field_success:
                raise Exception('Entered encrypted text and actual text are not equal !!!')

            if press_enter:
                time.sleep(5)
                element.send_keys(Keys.DOWN, Keys.ENTER)

    # ============================= Verify specific text in url method =============================
    def verify_current_url_contains_text(self, text: str) -> None:
        """ verify_url_contains_text method verify if the current URL contains the given text

            Method parameters:
              text -> contains text to be verified

            Return value -> None

        """

        current_url = self._web_driver.current_url
        assert text in current_url, f"'{current_url}' is not contains'{text}' text"

    # ============================= Scroll page to Top or Bottom method =============================
    def scroll_page_top_bottom(self, top_bottom: str = 'bottom') -> None:
        """ scroll_page_top_bottom method gives us an opportunity to scroll to Top or Bottom

            Method parameters:
              top_bottom -> contains top or bottom direction

            Return value -> None

        """

        print(f"===> Scrolling page to {top_bottom}")
        page = self._web_driver.find_element_by_tag_name('html')
        if top_bottom.lower() == 'top':
            page.send_keys(Keys.HOME)
        elif top_bottom.lower() == 'bottom':
            page.send_keys(Keys.END)
        else:
            raise Exception('Unsupported position!')

    # ================================== Switch to iframe method ==================================
    def switch_to_iframe(self, locator: str, vendor: str = '', list_index: int = 0, method: str = 'CSS') -> None:
        """ switch_to_iframe method gives us an opportunity to switch to iframe

            Method parameters:
               locator -> contains the name of the locator
               vendor -> contains the name of the vendor
               list_index -> contains index when we fetch list element
               method -> contains the method which will be used

            Return value -> None

        """

        frame = self.find_element(locator=locator, vendor=vendor, list_index=list_index, method=method)
        self._web_driver.switch_to.frame(frame)

    # =============================== Switch to default content method ===============================
    def switch_to_default_content(self) -> None:
        """ switch_to_default_content method gives us an opportunity to switch to default contain

            Method parameters -> None
            Return value -> None

        """

        self._web_driver.switch_to.default_content()

    # ============================= Select dropdown option by text method =============================
    def select_in_dropdown_by_text(self, text,  dropdown, method: str = 'CSS') -> None:
        """ select_in_dropdown_by_text method gives us an opportunity to
            select the dropdown option by using text

            Method parameters:
                text -> contains the text for dropdown selection
                dropdown -> contains the dropdown locator
                method -> contains the method which will be used for the selection

            Return value -> None

        """

        select = Select(self.find_element(dropdown, method))
        select.select_by_visible_text(text)

    # ============================= Select dropdown option by index method =============================
    def select_in_dropdown_by_index(self, index,  dropdown, method: str = 'CSS') -> None:
        """ select_in_dropdown_by_index method gives us an opportunity to
            select the dropdown option by using index

            Method parameters:
                index -> contains the index for dropdown selection
                dropdown -> contains the dropdown locator
                method -> contains the method which will be used for the selection

            Return value -> None

        """

        select = Select(self.find_element(dropdown, method))
        select.select_by_index(index)

    # ============================= Fetch element from vendor locators =============================
    def fetch_element_from_vendor_locators(self, element_name: str) -> object:
        """ fetch_element_from_vendor_locators method returns element from vendor locators file

            Method parameters:
                element_name -> contains the name of element

            Return value -> element value

        """

        try:
            element = locate('source.web_source.locators.%s.%s' % (self.resource_name_for_locators, element_name))
        except Exception as e:
            print(e)

        return element

    # ============================= Fetch web browser request info method =============================
    def fetch_web_browser_request_info(self, request_parameter: str) -> tuple:
        """ fetch_web_browser_request_info method fetch request information from the web browser

            Method parameters:
                request_parameter -> contains the request parameter

            Return value -> tuple with authorization token and case uuid

        """

        ui_case_uuid = ''
        ui_authorization_token = ''
        success_flag = False

        for request in self._web_driver.requests[::-1]:
            try:
                request_method = request.method
                request_url = request.url
                request_response_status_code = request.response.status_code
                request_headers_headers = request.headers._headers
            except AttributeError as atr_err:
                print(atr_err)
                continue

            if request_method == 'PATCH':
                if '/case-manager/cases/' in request_url:
                    if request_response_status_code == 200:
                        for parameters in request_headers_headers:
                            if parameters[0] == request_parameter:
                                ui_authorization_token = parameters[1].split()[-1]
                                break
                        ui_case_uuid = str(request).split('/')[-1]
            if ui_authorization_token != '' and ui_case_uuid != '':
                success_flag = True
                break
            else:
                continue

        if success_flag:
            return (ui_authorization_token, ui_case_uuid)
        else:
            raise Exception('Can not found ui_authorization token and/or case uuid in browser request info !!!')

    # ================================== Select Yes No button method ==================================
    @staticmethod
    def select_yes_or_no_button() -> str:
        """ select_yes_or_no_button static method which returns 'Yes' or 'No'

            Method parameters -> None

            Return value -> 'Yes' or 'No'

        """

        import random

        yes_no_selector_dict = {
            '0': 'Yes',
            '1': 'No'
        }

        return yes_no_selector_dict[str(random.randint(1, 100) % 2)]
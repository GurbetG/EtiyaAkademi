from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from constantsaucedemo import *


class Test_saucedemo:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.get(DOMAIN_URL)
        self.driver.maximize_window()
        self.today = str(date.today())
        Path(self.today).mkdir(exist_ok=True)
    
    def teardown_method(self):
        self.driver.quit()
    
    #Doğru bilgilerden standard_user kullanıcı adıyla giriş yapılmanın doğru olup olmadığı kontrol edilmelidir.
    def test_login(self):
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,USER_NAME_ID)))
        user= self.driver.find_element(By.ID, USER_NAME_ID )
        user.send_keys("standard_user")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,PASSWORD_NAME_ID)))        
        password= self.driver.find_element(By.ID, PASSWORD_NAME_ID )
        password.send_keys("secret_sauce")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,LOGIN_BUTTON_ID)))
        buton= self.driver.find_element(By.ID,LOGIN_BUTTON_ID)
        buton.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,MENU_BUTTON_ID)))
        menuButton= self.driver.find_element(By.ID,MENU_BUTTON_ID)
        menuText=menuButton.text

        assert menuText == MENU_TEXT


    #Yanlış bilgiler girildiğinde uyarı çıkıp çıkmadığı test edilmelidir.
    def wrong_login(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,USER_NAME_ID)))
        user= self.driver.find_element(By.ID, USER_NAME_ID )
        user.send_keys("standard_user")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,PASSWORD_NAME_ID)))
        password= self.driver.find_element(By.ID, PASSWORD_NAME_ID )
        password.send_keys("123456")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,LOGIN_BUTTON_ID)))
        buton= self.driver.find_element(By.ID,LOGIN_BUTTON_ID)
        buton.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,ERROR_LOGIN_XPATH)))
        errorButton= self.driver.find_element(By.XPATH,ERROR_LOGIN_XPATH)
        errorButtonSize = len(errorButton)

        assert errorButtonSize > 0 

    
    #Yanlış bilgiler girildiğinde çıkan uyarı mesajının doğruluğu kontrol edilmelidir Epic sadface: Username and password do not match any user in this service
    def error_message(self):
        self.wrong_login()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ERROR_LOGIN_XPATH)))
        errorMessage= self.driver.find_element(By.XPATH,ERROR_LOGIN_XPATH)
        errorMessageText = errorMessage.text

        assert errorMessageText == ERROR_TEXT

    #Ana sayfada 6 adet ürün listelendiği kontrol edilmelidir.
    def check_list(self):
        self.test_login()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,PRODUCT_lİST_XPATH)))
        product_check=self.driver.find_elements(By.XPATH,PRODUCT_lİST_XPATH)
        product_size=len(product_check)

        assert product_size==6

    #Sepete Ekle butonuna tıklandığında butonun texti REMOVE olmalıdır.
    def basket_remove(self):
        self.test_login()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,ADD_TO_CART_BUTTON_XPATH)))
        addToCartButton=self.driver.find_element(By.XPATH,ADD_TO_CART_BUTTON_XPATH)
        addToCartButton.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,REMOVE_BUTTON_XPATH)))
        removeButton=self.driver.find_element(By.XPATH,REMOVE_BUTTON_XPATH)
        removeText=removeButton.text

        assert removeText==REMOVE_TEXT

    #Sepete 1 adet ürün eklendiğinde sağ üstteki sepet üzerinden 1 sayısı çıkmalıdır.
    def number_of_product(self):
        self.test_login()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,ADD_TO_CART_BUTTON_XPATH)))
        addToCartButton=self.driver.find_element(By.XPATH,ADD_TO_CART_BUTTON_XPATH)
        addToCartButton.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,PRODUCT_NUMBER_XPATH)))
        productNumber=self.driver.find_element(By.XPATH,PRODUCT_NUMBER_XPATH)
        productNumberText=productNumber.text

        assert productNumberText==PRODUCT_NUMBER_TEXT


        




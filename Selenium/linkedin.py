from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#yanlış kullanıcı,şifre test
driver=webdriver.Chrome()
driver.get("https://tr.linkedin.com/")
driver.maximize_window()
sleep(2)
input=driver.find_element(By.NAME,'session_key')
input.send_keys("deneme")
sleep(2)
password=driver.find_element(By.NAME,'session_password')
password.send_keys("1234")
sleep(2)
buton=driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form/button")
buton.click()
sleep(3)
title = driver.title
if  title=="(1) Akış | LinkedIn":
    print("Giriş başarılı ✅")
else:
    print("Giriş başarısız!❌") 
sleep(2) 

#doğru kullanıcı,şifre test
driver=webdriver.Chrome()
driver.get("https://tr.linkedin.com/")
driver.maximize_window()

input=driver.find_element(By.NAME,'session_key')
input.send_keys("gurbetyildiz@gmail.com")
sleep(2)
password=driver.find_element(By.NAME,'session_password')
password.send_keys("30031985")
sleep(2)
buton=driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form/button")
buton.click()
sleep(3)

title = driver.title
if  title=="Jobs | LinkedIn":
    print("Giriş başarılı ✅")
else:
    print("Giriş başarısız!❌") 
sleep(2) 












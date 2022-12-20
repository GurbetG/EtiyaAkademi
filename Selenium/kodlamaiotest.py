from datetime import date
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.kodlama.io/")
driver.maximize_window()

totalcourse=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]")
driver.save_screenshot(str(date.today()) + '(1).png')

searchbox=driver.find_element(By.NAME,"query")
searchbox.send_keys("senior")

title = driver.find_element(By.XPATH,'//*[@title="Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)"]')
titleTest = title.text

if titleTest == "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)":
    print("Arama Testi Başarılı✅")
else:
    print("Arama Testi Başarısız❌")
driver.save_screenshot(str(date.today()) + '(2).png')
sleep(2)

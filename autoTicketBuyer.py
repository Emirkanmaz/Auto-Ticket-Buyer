import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=r"D:\chromedriver\chromedriver.exe")  # driver location
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.passo.com.tr/tr/giris")
time.sleep(2)

username = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-login/section/div/div/div/div/div[2]/div/div/div[1]/div/quick-form/div/quick-input[1]/input')
password = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-login/section/div/div/div/div/div[2]/div/div/div[1]/div/quick-form/div/quick-input[2]/input')
girisbt = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-login/section/div/div/div/div/div[2]/div/div/div[1]/div/quick-form/div/div[2]/button[2]')
username.send_keys("")  # username here
password.send_keys("")  # password here
girisbt.click()
time.sleep(3)


driver.get("https://www.passo.com.tr/tr/etkinlik/kardelen-salon-iksv-konser-biletleri/4008321/koltuk-secim")  # link here with seat selection at end
time.sleep(3)

while True:
    try:
        ogrenci = Select(driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-seat/div/div[3]/div/div[2]/div[2]/div[3]/div/select"))
        ogrenci.select_by_value("3: Object")
        time.sleep(1)
        eczaci = driver.find_element(By.XPATH, "/html/body/app-root/passo-priority-sale/div/div/div/div[2]/div[3]/div/div/div[3]/div/input")
        eczaci.click()
        eczaci.send_keys("eczacibasigencbilet")
        dvmbtn = driver.find_element(By.XPATH, "/html/body/app-root/passo-priority-sale/div/div/div/div[3]/button[1]")
        dvmbtn.click()
        time.sleep(1)
        bilet = Select(driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-seat/div/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div/div/div/select"))
        bilet.select_by_visible_text("1")
        time.sleep(1)
        tmmbtn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[1]")
        tmmbtn.click()
        time.sleep(1)
        blok = Select(driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-seat/div/div[3]/div/div[2]/div[4]/select"))
        blok.select_by_value("1: Object")
        dvmbtn0 = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-seat/div/div[3]/div/div[2]/div[5]/div[3]/div/button")
        dvmbtn0.click()
    except:
        driver.refresh()
        driver.implicitly_wait(5)
    else:
        break

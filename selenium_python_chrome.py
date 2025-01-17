# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)
import time

from selenium.webdriver import ActionChains
# импортируем необходимые библиотеки и элементы
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'http://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

# создаем переменную для кнопки под двойной клик, нажимаем её и проверяем активацию
action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()
print('Произвели двойной клик')

# создаем переменную для кнопки под правый клик, нажимаем её и проверяем активацию
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()
print('Произвели правый клик')
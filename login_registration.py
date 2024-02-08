
22222222222222222222222222222222222222222222222222222222222222222222222222222222

# (2).Registration_login: регистрация аккаунта
# 1. Откройте
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Нажмите на вкладку "My Account Menu"
my_account=driver.find_element_by_css_selector("#main-nav.main-nav>li:nth-child(2)").click()
# 3. В разделе "Register", введите email для регистрации
reg_email=driver.find_element_by_css_selector("#reg_email").send_keys('Olesya@mail.ru')
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
reg_password=driver.find_element_by_css_selector("#reg_password").send_keys('Olesya312Ole')
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
wait=WebDriverWait(driver,20)
strong=wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME,'strong'),'Strong')
)
# 5. Нажмите на кнопку "Register"
register=driver.find_element_by_css_selector('.woocommerce-Button[value="Register"]').click()
import time
driver.quit()

33333333333333333333333333333333333333333333333333333333333

# (3).Registration_login: логин в систему
# 1. Откройте http://practice.automationtesting.in/
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Нажмите на вкладку "My Account Menu"
my_account=my_account=driver.find_element_by_css_selector("#main-nav.main-nav>li:nth-child(2)").click()
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
email=driver.find_element_by_css_selector("#username").send_keys('Olesya@mail.ru')
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
password=driver.find_element_by_css_selector("#password").send_keys('Olesya312Ole')
# 5. Нажмите на кнопку "Login"
login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# 6. Добавьте проверку, что на странице есть элемент "Logout"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait=WebDriverWait(driver, 10)
logout=wait.until(
   EC.element_to_be_clickable((By.CSS_SELECTOR,
'[href="https://practice.automationtesting.in/my-account/customer-logout/"]:nth-child(1)'))
)
driver.quit()



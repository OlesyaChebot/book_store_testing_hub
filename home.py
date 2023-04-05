
#111111111111111111111111111111111111111111111111111111111111111111111111111

#  Home: добавление комментария
# 1. Откройте http://practice.automationtesting.in/
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selen_ruby=driver.find_element_by_css_selector(".product_tag-selenium").click()
# 4. Нажмите на вкладку "REVIEWS"
tab_rev=driver.find_element_by_css_selector(".reviews_tab").click()
# 5. Поставьте 5 звёзд
stars=driver.find_element_by_css_selector('.stars a:nth-child(5)').click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
comment=driver.find_element_by_css_selector('#comment').send_keys('Nice book!')
# 7. Заполните поле "Name"
name=driver.find_element_by_css_selector('#author').send_keys('Olesya')
# 8. Заполните "Email"
email=driver.find_element_by_css_selector('#email').send_keys('Olesya@mail.ru')
# 9. Нажмите на кнопку "SUBMIT"
submit=driver.find_element_by_css_selector('.submit#submit').click()
driver.quit()

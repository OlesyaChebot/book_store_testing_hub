
44444444444444444444444444444444444444444444444444444444444444444444444444444444444444

# (4) Shop: отображение страницы товара
# 1. Откройте http://practice.automationtesting.in/
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Залогиньтесь
my_account=my_account=driver.find_element_by_css_selector("#main-nav.main-nav>li:nth-child(2)").click()
email=driver.find_element_by_css_selector("#username").send_keys('Olesya@mail.ru')
password=driver.find_element_by_css_selector("#password").send_keys('Olesya312Ole')
login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# 3. Нажмите на вкладку "Shop"
shop=driver.find_element_by_id('menu-item-40').click()
# 4. Откройте книгу "HTML 5 Forms"
html5=driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
title=driver.find_element_by_css_selector('.summary .product_title').text
title=="HTML5 Forms"
driver.quit()


55555555555555555555555555555555555555555555555555555555555555555555555555555555
#  (5)Shop: количество товаров в категории
# 1. Откройте http://practice.automationtesting.in/
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Залогиньтесь
my_account=my_account=driver.find_element_by_css_selector("#main-nav.main-nav>li:nth-child(2)").click()
email=driver.find_element_by_css_selector("#username").send_keys('Olesya@mail.ru')
password=driver.find_element_by_css_selector("#password").send_keys('Olesya312Ole')
login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# 3. Нажмите на вкладку "Shop"
shop=driver.find_element_by_id('menu-item-40').click()
# 4. Откройте категорию "HTML"
html_cat=driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]').click()
# 5. Добавьте тест, что отображается три товара
prod_count=driver.find_elements_by_css_selector('.product.type-product')
if len(prod_count) == 3:
    print("В корзине 3 товара")
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))
driver.quit()


6666666666666666666666666666666666666666666666666666666666666666666666666666666666
# (6) Shop: сортировка товаров
# 1. Откройте http://practice.automationtesting.in/
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Залогиньтесь
my_account=my_account=driver.find_element_by_css_selector("#main-nav.main-nav>li:nth-child(2)").click()
email=driver.find_element_by_css_selector("#username").send_keys('Olesya@mail.ru')
password=driver.find_element_by_css_selector("#password").send_keys('Olesya312Ole')
login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# 3. Нажмите на вкладку "Shop"
shop=driver.find_element_by_id('menu-item-40').click()
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
sort=driver.find_element_by_css_selector('.orderby [selected="selected"]')
sort_value=sort.get_attribute('value')
assert sort_value == "menu_order"
# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
from selenium.webdriver.support.select import Select
sort_price=driver.find_element_by_class_name('orderby')
select=Select(sort_price)
select.select_by_value("price-desc")
# 6. Снова объявите переменную с локатором основного селектора сортировки
# т.к после сортировки страница обновится
sort=driver.find_element_by_css_selector('.orderby [selected="selected"]')
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value
sort_value2=sort.get_attribute('value')
assert sort_value2=="price-desc"
driver.quit()

777777777777777777777777777777777777777777777777777777777777777777777777777777777777

# (7) Shop: отображение, скидка товара
# 1. Откройте http://practice.automationtesting.in/
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Залогиньтесь
my_account=my_account=driver.find_element_by_css_selector("#main-nav.main-nav>li:nth-child(2)").click()
email=driver.find_element_by_css_selector("#username").send_keys('Olesya')
password=driver.find_element_by_css_selector("#password").send_keys('Olesya312Ole')
login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# 3. Нажмите на вкладку "Shop"
shop=driver.find_element_by_id('menu-item-40').click()
# 4. Откройте книгу "Android Quick Start Guide"
android=driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
old_price=driver.find_element_by_xpath("//del//span[@class='woocommerce-Price-amount amount']")
text_old_price=old_price.text
# assert text_old_price == "₹600.00"
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
new_price=driver.find_element_by_xpath("//ins//span[@class='woocommerce-Price-amount amount']")
text_new_price=new_price.text
assert text_new_price == "₹450.00"
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки
# (не вся картинка на всю страницу)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait=WebDriverWait(driver, 20)
cover=wait.until(
   EC.presence_of_element_located((By.CSS_SELECTOR,'[title="Android Quick Start Guide"]'))
).click()
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close=wait.until(
   EC.element_to_be_clickable((By.CLASS_NAME,'pp_close'))
).click()
driver.quit()

888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# (8)  Shop: проверка цены в корзине
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Нажмите на вкладку "Shop"
shop=driver.find_element_by_id('menu-item-40').click()
# 3. Добавьте в корзину книгу "Mastering JavaScript" # см. комментарии в самом низу
book=driver.find_element_by_css_selector('[title="Mastering JavaScript"]').click()
add_bskt=driver.find_element_by_css_selector('.single_add_to_cart_button').click()
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹350.00"
# • Используйте для проверки assert
bskt_count=driver.find_element_by_class_name('cartcontents').text
assert bskt_count=="1 Item"
cost=driver.find_element_by_css_selector('[class="amount"]')
cost_text=cost.text
assert cost_text=="₹350.00"
# 5. Перейдите в корзину
cost.click()
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait=WebDriverWait(driver, 10)
subtotal=wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[data-title="Subtotal"]'), "₹350.00")
)
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
total=wait.until(
    EC.presence_of_element_located((By.XPATH,'//tr[@class="order-total"]/./td[@data-title="Total"]'))
)
driver.quit()

99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

#  (9) Shop: работа в корзине
# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента,
# этот сценарий один из таких, используйте time.sleep()
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# # 2. Нажмите на вкладку "Shop"
shop=driver.find_element_by_id('menu-item-40').click()
# 3. Добавьте в корзину книгу, которую можно добавить
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
book=driver.find_element_by_css_selector('[title="Mastering JavaScript"]').click()
add_bskt=driver.find_element_by_css_selector('.single_add_to_cart_button').click()
import time
time.sleep(5)
# 4. Перейдите в корзину
cost=driver.find_element_by_css_selector('[class="amount"]').click()
# 5. Удалите книгу
# • Перед удалением добавьте sleep
time.sleep(5)
remove=driver.find_element_by_class_name('remove').click()
# 6. Нажмите на Undo (отмена удаления)
undo=driver.find_element_by_xpath('//div[@class="woocommerce-message"]/a').click()
# 7. В Quantity увеличьте количесто товара до 3 шт
# • Предварительно очистите поле с помощью локатор_поля.clear()
quantity_field=driver.find_element_by_css_selector(".quantity>input")
quantity_field.clear()
quantity_field.send_keys(3)
# 8. Нажмите на кнопку "UPDATE BASKET"
upd_btn=driver.find_element_by_css_selector('[value="Update Basket"]').click()
# 9. Добавьте тест, что value элемента quantity
# для "JS Data Structures and Algorithm" равно 3 # используйте assert
quantity_field2=driver.find_element_by_css_selector(".quantity>input")
quantity_num=quantity_field2.get_attribute("value")
assert quantity_num=="3"
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
time.sleep(5)
apply_btn=driver.find_element_by_css_selector('[value="Apply Coupon"]').click()
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
coupon=driver.find_element_by_css_selector('.woocommerce-error').text
assert coupon=="Please enter a coupon code."
driver.quit()

10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10

# (10) Shop: покупка товара
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://practice.automationtesting.in/')
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop=driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
# 3. Добавьте в корзину книгу
buy=driver.find_element_by_css_selector('[data-product_id="165"]').click()
# 4. Перейдите в корзину
import time
time.sleep(5)
cart=driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0').click()
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
wait=WebDriverWait(driver, 10)
chk_out=wait.until(
EC.element_to_be_clickable((By.CSS_SELECTOR,'[href="https://practice.automationtesting.in/checkout/"]'))
)
chk_out.click()
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
#Проверка наличия сообщения о возможности залогиниться
showlogin=wait.until(
EC.presence_of_element_located((By.CSS_SELECTOR,'.showlogin'))
)
#Проверка наличия сообщения о возможности применить купон
showcoupon=wait.until(
EC.presence_of_element_located((By.CSS_SELECTOR,'.showcoupon'))
)
#Проверка наличия пометок обязательности полей в виде звездочки
star_in_f_n=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_first_name"]>abbr'), '*')
)
star_in_s_n=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_last_name"]>abbr'), '*')
)
star_in_email=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_email"]>abbr'), '*')
)
star_in_phone=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_phone"]>abbr'), '*')
)
star_in_country=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_country"]>abbr'), '*')
)
star_in_address=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_address_1"]>abbr'), '*')
)
star_in_city=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_city"]>abbr'), '*')
)
star_in_state=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_state"]>abbr'), '*')
)
star_in_postcode=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[for="billing_postcode"]>abbr'), '*')
)
# Заполнение обязательных полей
first_name=driver.find_element_by_css_selector('#billing_first_name').send_keys('Olesya')
s_n=driver.find_element(By.CSS_SELECTOR,'#billing_last_name').send_keys('Che')
email=driver.find_element(By.CSS_SELECTOR,'#billing_email').send_keys('Olesya@mail.ru')
phone=driver.find_element(By.CSS_SELECTOR,'#billing_phone').send_keys('88125982525')
country=driver.find_element(By.CSS_SELECTOR,'#s2id_billing_country').click()
country2=driver.find_element(By.CSS_SELECTOR,'#s2id_autogen1_search').send_keys('russ')
country_select=driver.find_element(By.CSS_SELECTOR,'.select2-match').click()
address1=driver.find_element(By.CSS_SELECTOR,'[placeholder="Street address"]').send_keys('Dalya st.')
address2=driver.find_element(By.CSS_SELECTOR,'[placeholder="Apartment, suite, unit etc. (optional)"]')
address2.send_keys('1')
city=driver.find_element(By.CSS_SELECTOR,'[name="billing_city"]').send_keys('S.-Petersburg')
county=driver.find_element(By.CSS_SELECTOR,'[name="billing_state"]#billing_state').send_keys('S.-Petersburg')
postcode=driver.find_element(By.CSS_SELECTOR,'[name="billing_postcode"]').send_keys('812')
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - >
# нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё,
# затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check=driver.find_element(By.CSS_SELECTOR,'[value="cheque"]').click()
# 8. Нажмите PLACE ORDER
place_order=driver.find_element(By.CSS_SELECTOR,'#place_order').click()
# 9. Используя явное ожидание, проверьте что отображается надпись
# "Thank you. Your order has been received."
text1=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.page-content.entry-content'),"Thank you. Your order has been received.")
)
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
text2=wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.shop_table.order_details>tfoot>tr:nth-child(3)>td'),"Check Payments")
)
driver.quit()

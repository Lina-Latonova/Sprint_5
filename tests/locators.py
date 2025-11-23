from selenium.webdriver.common.by import By

class Locators:
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  # Поле для ввода имени
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")  # Поле для ввода email
    PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input")  # Поле для ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button")  # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.ID, "//*[@id='root']/div/main/div/form/fieldset[2]/div/p") # Сообщение об ошибке пароля
    BUTTON_CONSTRUCTOR  = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a")  # Кнопка "Конструктор"
    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # Кнопка "Войти в аккаунт" на главной
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a") # Заголовок конструтора "Собери бургер"
    TEXT_HEADER = (By.XPATH, "//*[@id='root']/div/main/div/nav/p") 
    EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') # Поле для ввода имени
    PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') # Поле для ввода email
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Кнопка "Зарегистрироваться"
    CONSTRUCTOR_HEADER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1') # Заголовок "Соберите бургер"
    ACCOUNT_HEADER = (By.XPATH, '//*[@id="root"]/div/header/nav/a') # Кнопка "Личный кабинет" в хедере
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button') # Кнопка "Войти в аккаунт" на главной
    HEADER_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p') # Заголовок кнопка "Личный кабинет" в хедере
    EXIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') # Кнопка "Выход" в личном кабинете
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') #
    STELLAR_BURGERS = (By.XPATH, '//*[@id="root"]/div/header/nav/div') # логотип
    FILLING_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]') # Кнопка "Начинки" на главной
    FILLING_HEADER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]') # Наименование раздела "Начинки" 
    SAUCE_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]') # Кнопка "Соусы" на главной
    SAUCE_HEADER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]') # Наименование раздела "Соусы"
    BREAD_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]') # Кнопка "Булки" на главной
    BREAD_HEADER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]') # Наименование раздела "Булки"
   
from selenium.webdriver.common.by import By

class Locators:
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле для ввода имени
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле для ввода email
    PASSWORD_FIELD = (By.XPATH, ".//input[@type = 'password']")  # Поле для ввода пароля
    EMAIL_REG = (By.XPATH, "//label[text()='Email']/parent::div/input")
    PASSWORD_REG = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']") # Сообщение об ошибке пароля
    BUTTON_CONSTRUCTOR  = (By.LINK_TEXT, "Конструктор")  # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.CLASS_NAME, "text_type_main-large") # Заголовок конструтора "Собери бургер"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной
    HEADER_LOGIN_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Заголовок кнопка "Личный кабинет" в хедере
    STELLAR_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Основной логотип
    
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    FILLING_BUTTON = (By.XPATH, "//span[text()='Начинки']") # Кнопка "Начинки" на главной
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']") # Кнопка "Соусы" на главной =
    BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']") # Кнопка "Булки" на главной
    FILLING_HEADER = (By.XPATH, "//h2[text()='Начинки']")  # Наименование раздела "Начинки"
    SAUCE_HEADER = (By.XPATH, "//h2[text()='Соусы']") # Раздел "Соусы"
    BREAD_HEADER = (By.XPATH, "//h2[text()='Булки']") # Наименование раздела "Булки"
    ERROR_MESSAGE = (By.XPATH, "//p[.='Некорректный пароль']")
   
    EXIT_BUTTON = (By.XPATH, "//button[@type='button' and @class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']") # Кнопка "Выход" в личном кабинете
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # Кнопка Войти на страницы регистрации
    ACCOUNT_HEADER = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']") # Кнопка "Личный кабинет" в хедере
    ENTER_HEADER = (By.XPATH, "//h2[text()='Вход']") # Заголовок Вход на странице регистрации
   
    ACCOUNT_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']") # Уже зарегистрированы? Войти - кнопка
    PROFILE_NAV = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='Профиль']")
    selected_button = By.XPATH, ('//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') # Селектор, помечающий выбранный раздел конструктора как активный
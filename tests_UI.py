import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def web_driver():
    driver = webdriver.Chrome()
    # Переходим на страницу сайта визитки
    driver.get('https://dima731515.github.io/hakaton/html/')

    yield driver

    driver.quit()


""""Тест на проверку работы  кнопки 'Смотреть на youtube'"""


def test_button_youtube(web_driver):
    time.sleep(3)
    # нажимаем на кнопку "Смотреть на youtube"
    web_driver.find_element(By.CSS_SELECTOR, 'body > main > section.hero.hero_desctop.container > a > div > p').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://www.youtube.com/@pleasantildar'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)


""""Тест на проверку работы  кнопки соц.сетей youtube"""


def test_button_social_networks_youtube(web_driver):
    time.sleep(3)
    # нажимаем на кнопку соц.сетей  "youtube"
    web_driver.find_element(By.XPATH, '/html/body/header/a[1]/img').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://www.youtube.com/@pleasantildar'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)


""""Тест на проверку работы  кнопки соц.сетей Twitch"""


def test_button_social_networks_twitch(web_driver):
    time.sleep(3)
    # нажимаем на кнопку соц.сетей  "twitch"
    web_driver.find_element(By.XPATH, '/html/body/header/a[2]/img').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://www.twitch.tv/ildarzhe'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)


""""Тест на проверку работы  кнопки соц.сетей Twitch"""


def test_button_social_networks_telegram(web_driver):
    time.sleep(3)
    # нажимаем на кнопку соц.сетей  "Telegram"
    web_driver.find_element(By.XPATH, '/html/body/header/a[3]/img').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://www.t.me/unpleasent'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)


""""Тест на проверку работы  кнопки соц.сетей instagram"""


def test_button_social_networks_instagram(web_driver):
    time.sleep(3)
    # нажимаем на кнопку соц.сетей  "instagram"
    web_driver.find_element(By.XPATH, '/html/body/header/a[4]/img').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://www.instagram.com/masterildar/'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)


""""Тест на проверку работы  кнопки соц.сетей twitter"""


def test_button_social_networks_twitter(web_driver):
    time.sleep(3)
    # нажимаем на кнопку соц.сетей  "twitter"
    web_driver.find_element(By.XPATH, '/html/body/header/a[5]/img').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://twitter.com/master_ildar' \
           or web_driver.current_url == 'https://twitter.com/i/flow/login?redirect_after_login=%2Fmaster_ildar'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)


""""Тест на проверку работы  кнопки соц.сетей VK"""


def test_button_social_networks_vk(web_driver):
    time.sleep(3)
    # нажимаем на кнопку соц.сетей  "VK"
    web_driver.find_element(By.XPATH, '/html/body/header/a[6]/img').click()
    time.sleep(3)
    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle
    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])
    # Подтверждение URL
    assert web_driver.current_url == 'https://vk.com/pleasentildar'
    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)




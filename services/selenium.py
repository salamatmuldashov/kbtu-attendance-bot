from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_driver():
    options = Options()
    options.add_argument("--headless") # Можно отключить для отладки
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    
    # ОБЯЗАТЕЛЬНО: переместите exeшник chromedriver в корень проекта
    service = Service("./chromedriver")  # или chromedriver.exe на Windows
    return webdriver.Chrome(service=service, options=options)
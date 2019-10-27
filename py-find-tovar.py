from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

urls = "https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/"

# флаг скрытого запуска браузера
hidden = False 

# настройки скрытого режима хрома
WINDOW_SIZE = "1920,1080"
chrome_options = Options()  
if(hidden):
    chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# END настройки скрытого режима хрома

driver = webdriver.Chrome(chrome_options=chrome_options,  executable_path='./drv/chromedriver')
driver.get(urls)

#elem_secret_level = driver.find_elements_by_css_selector('div[class="auth"]')
#print("Elem Secret Level = ", elem_secret_level)
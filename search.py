import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

def get_results(search_term):
    url = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/"
    browser = webdriver.Chrome()
    browser.get(url)
    try:
        #search_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/form[1]/input[1]")))
        search_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "input1")))
        ActionChains(browser).move_to_element(search_box).click().send_keys(search_term).perform()
        submit_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='搜索']")))
        submit_button.click()
        results_table = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//table[@class='search-results']")))
        Links = results_table.find_elements_by_xpath("/html/body/form/table[1]/tbody/tr[2]/td[1]/font[3]")
        results = [link.text for link in Links]
    except TimeoutException:
        print("Timed out waiting for search box to load")
        results = []
    finally:
        browser.close()   
    return results


get_results("行")
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

KEYWORDS = [
        "RACA",
        "Radio",
        "Caca"
        ]

def get_announcement_title(driver, index, page):
    title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, f"link-0-{ index }-p{ page }"))).text
    return title

def get_announcement_link(driver, index, page):
    link = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, f"link-0-{ index }-p{ page }"))).get_attribute('href')
    return link


def get_announcement_article(driver):
    article = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, "article"))).text
    return article

def get_announcement_date(driver):
    # try:
        # date = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-17s7mnd"))).text
    # except:
        # date = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1ebhcfx"))).text
    # return date
    return None

def check_keywords(title, article, keyword):
    for keyword in KEYWORDS:
        if keyword.lower() in title.lower() or keyword.lower() in article.lower():
            return True
    return False


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
announcements = []

with driver:
    driver.get('https://www.binance.com/en/support/announcement/c-48/')
    driver.execute_script("window.open('about:blank');")

    announcements = []

    for index in range(0, 15):
        driver.switch_to.window(driver.window_handles[0])

        title = get_announcement_title(driver, index, 1)
        link = get_announcement_link(driver, index, 1)

        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)

        article = get_announcement_article(driver)
        date = get_announcement_date(driver)

        announcements.append(
                {
                    "title": title, 
                    "link": link,
                    "article": article,
                    "date": date
                    }
                )

    for announcement in announcements:
        new = check_keywords(announcement["title"], announcement["article"], KEYWORDS)
        if new == True:
            print("Coin is available!")
        elif new == False:
            print("Not yet!")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_title(driver, index, page):
    title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, f"link-0-{index}-p{page}"))).text
    return title


def get_link(driver, index, page):
    link = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, f"link-0-{index}-p{page}"))).get_attribute('href')
    return link


def get_article(driver):
    article = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, "article"))).text
    return article


def get_date(driver):
    # try:
    # date = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-17s7mnd"))).text
    # except:
    # date = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1ebhcfx"))).text
    # return date
    return None


def check_keywords(title, article, keywords):
    for keyword in keywords:
        if keyword.lower() in title.lower() or keyword.lower() in article.lower():
            return True
    return False


def get_driver():
    options = Options()
    options.headless = True
    return webdriver.Firefox(options=options)


def get_all(driver):
    announcements = []

    with driver:
        driver.get('https://www.binance.com/en/support/announcement/c-48/')
        driver.execute_script("window.open('about:blank');")

        for index in range(0, 15):
            driver.switch_to.window(driver.window_handles[0])

            title = get_title(driver, index, 1)
            link = get_link(driver, index, 1)

            driver.switch_to.window(driver.window_handles[1])
            driver.get(link)

            article = get_article(driver)
            date = get_date(driver)

            announcements.append(
                {
                    "title": title,
                    "link": link,
                    "article": article,
                    "date": date
                }
            )

    return announcements

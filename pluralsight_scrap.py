# pluralsight.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    driver = webdriver.Chrome(executable_path="D:\Projects\Git_WS\chromedriver_win32\chromedriver.exe", options = chrome_options)
    return driver


def getCources(driver, search_keyword):
    # Step 1: Go to pluralsight.com
    driver.get("https://www.pluralsight.com/")
    # Step 2: Search for input xpath and fill-in the keyword and press enter
    search_input_xpath = "//*[@id='header_searchForm']/input[1]"
    search_input = driver.find_element_by_xpath(search_input_xpath)
    search_input.send_keys(search_keyword)
    search_input.send_keys(Keys.ENTER)

    # Step 3: Create a parse tree of page sources after searching
    soup = BeautifulSoup(driver.page_source, "lxml")
    # Step 4: Iterate over the search result and fetch the course
    search_result = soup.select_one("div.search-results-section div.search-results-rows")
    for course in search_result.select("div.search-result"):
        title_selector = "div.search-result__info div.search-result__title a"
        author_selector = "div.search-result__details div.search-result__author"
        level_selector = "div.search-result__details div.search-result__level"
        length_selector = "div.search-result__details div.search-result__length"
        print({
            "title": course.select_one(title_selector).text,
            "author": course.select_one(author_selector).text,
            "level": course.select_one(level_selector).text,
            "length": course.select_one(length_selector).text,
        })

# create the driver object.
driver = configure_driver()
search_keyword = "Web Scraping"
getCources(driver, search_keyword)
# close the driver.
driver.close()
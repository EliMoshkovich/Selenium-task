from SeleniumTask import *


def main():

    " For Generic program, the values are here and can be changed as needed "

    # browser driver path
    driver_path = "chromedriver/chromedriver.exe"

    # what to search
    search_string = "Claroty"
    # search engine website
    search_engine = "https://www.google.com/"

    # URL of our website
    url_first_link = "https://www.claroty.com/"

    # URL for claroty's careers
    careers_url = "https://www.claroty.com/careers"

    # All the program's functions
    browser_driver = driverInitialize(driver_path)
    resultsNumber(browser_driver, search_string, search_engine)
    firstLink(browser_driver, url_first_link)
    clarotyJobs(browser_driver,  careers_url)
    exit(browser_driver)


if __name__ == "__main__":
    # execute only if run as a script
    main()


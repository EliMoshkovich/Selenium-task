from SeleniumTask import *


def main():

    " Starting the task  "

    browser_driver = driverInitialize()
    resultsNumber(browser_driver)
    firstLink(browser_driver)
    clarotyJobs(browser_driver)
    exit(browser_driver)


if __name__ == "__main__":
    # execute only if run as a script
    main()


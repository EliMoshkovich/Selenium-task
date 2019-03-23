from SeleniumTask import *


def program():

    " Starting the task  "

    browser_driver = driverInitialize()
    resultsNumber(browser_driver)
    firstLink(browser_driver)
    clarotyJobs(browser_driver)
    exit(browser_driver)


program()

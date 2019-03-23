import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def driverInitialize():

    "Please replace the driver_path below according to your own driver location"

    # driver path
    driver_path = "chromedriver/chromedriver.exe"

    # driver can by changed according to browser driver
    driver = webdriver.Chrome(driver_path)
    return driver

def resultsNumber(driver):

    "Function will search claroty at google and print to console results number"

    # Can be changed if need
    search_string = "Claroty"

    # open google
    driver.get("https://www.google.com/")
    # locate the search field
    search = driver.find_element_by_name('q')
    # type "Claroty" into search field
    search.send_keys(search_string)
    # hit return after you enter search text
    search.send_keys(Keys.RETURN)
    # locate the resultStats element
    result_str = driver.find_element_by_id('resultStats')
    # using regex for get only integer result
    res_dig = int(''.join(elem for elem in re.findall(r'\d*', re.sub(r'\(.*?\)', '', result_str.text)) if elem.isdigit()))
    # print the text of resultStats
    print("Results number by google search for Claroty is about: " , res_dig)

def firstLink(driver):

    "Function will check if claroty.com is the first results link"

    # URL can be changed if need
    url = "https://www.claroty.com/"

    # finds webresults
    links_list = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')
    # clicks the first link
    links_list[0].click()
    # check if link is claroty.com
    if driver.current_url == url:
        print(driver.current_url , 'Is the first link of google search results')
    else:
        print("https://www.claroty.com/  Is not the first link of google search results")

def clarotyJobs(driver):

    "Function will check how many visible jobs exist at careers page"

    driver.get("https://www.claroty.com/careers")
    elements = driver.find_elements_by_class_name('w-dyn-item')
    numberOfVisibleItems = 0
    for item in elements:
        children = item.find_elements_by_xpath('div')
        for child in children:
            classString = child.get_attribute('class')
            if "w-condition-invisible" not in classString:
                numberOfVisibleItems = numberOfVisibleItems + 1
                break
    print("number of carriers available:",  numberOfVisibleItems)




def exit(driver):

    "Function will give us few sec to see the browser and then will close him"

    # sleep for 5 seconds so you can see the results
    time.sleep(5)
    # Close the browser
    driver.quit()












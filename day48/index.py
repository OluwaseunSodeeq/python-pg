from selenium import webdriver
cgrome_driver_path = "/users/rafael/Downloads/chromedriver"
driver = webdriver.Chrome(cgrome_driver_path)

driver.get("https://www.google.com")
# price = driver.find_element__by_id('priceblock_ourprice')
# print(price.text)


search_bar = driver.find_element_by_name("q")
print(search_bar.tag_name)

driver.quit()
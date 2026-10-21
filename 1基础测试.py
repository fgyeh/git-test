from selenium import webdriver

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()
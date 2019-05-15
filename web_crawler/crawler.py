from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.set_window_size(1920, 1080)
print (driver.get_window_size())

driver.get("https://www.cwb.gov.tw/V8/C/P/Rainfall/Rainfall_10Min_County.html")

select = Select(driver.find_element_by_xpath("//select[@id='scity']"))
select.select_by_visible_text("新北市")
driver.save_screenshot("screenshot.png")
driver.close()
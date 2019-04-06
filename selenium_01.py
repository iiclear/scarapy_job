from selenium import webdriver
import time
options =webdriver.FirefoxOptions()
options.add_argument('-headless')
driver =webdriver.Firefox(executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver',options=options)
driver.implicitly_wait(20)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)
for i in range(0,3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    load_more = driver.find_element_by_css_selector('button.more-btn')
    load_more.click()
    driver.switch_to.default_content()
    time.sleep(2)

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)
from selenium import webdriver

class Browser(object):

    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

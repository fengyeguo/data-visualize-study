from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/JqueryProgressBar.html")

    # 执行一些操作，例如点击按钮或输入文本
    button = driver.find_element(By.XPATH, '//*[@id="downloadButton"]')
    button.click()

    # 显式等待，等待某个元素出现
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'progress-label'))
    )

    # 自定义等待条件，等待元素的文本变为期望的内容
    class TextToBePresentInElement:
        def __init__(self, locator, text_):
            self.locator = locator
            self.text = text_

        def __call__(self, driver):
            element = driver.find_element(*self.locator)
            return self.text in element.text

    # 定位目标元素
    target_locator = (By.CLASS_NAME, 'progress-label')
    expected_text = 'Complete!'

    # 显式等待，直到目标元素的文本变为期望的内容
    WebDriverWait(driver, 10).until(
        TextToBePresentInElement(target_locator, expected_text)
    )

    # 在这里可以继续执行其他操作
    print("操作完成，元素的文本已变为期望的内容。")
finally:
    # 退出浏览器
    driver.quit()

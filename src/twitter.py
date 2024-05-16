import chromedriver_autoinstaller
from selenium import webdriver
import time
from PIL import Image
import io
import json

def take_screenshot(url, index):
    chromedriver_autoinstaller.install()
    # Set up Selenium WebDriver (make sure you have the appropriate driver installed, e.g., chromedriver)
    driver = webdriver.Chrome()

    # Navigate to the webpage
    driver.get(url)
    driver.set_window_size(800, 2000)
    time.sleep(10)

    element_to_hide = driver.find_element_by_xpath('//*[@data-testid="BottomBar"]')
    driver.execute_script('arguments[0].style.visibility = "hidden";', element_to_hide)

    element = driver.find_element_by_xpath('//*[@data-testid="cellInnerDiv"]')

    location = element.location
    size = element.size

    # Take a screenshot of the entire page
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(io.BytesIO(screenshot))

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    element_screenshot = screenshot.crop((left, top, right, bottom))

    element_screenshot.save(f'./data/screenshot_twitter_{index}.png')

    driver.quit()


def arrayUrl(file):
    with open (file, 'r') as file:
        datas = json.load(file)
    for i, data in enumerate(datas):
        print(data)
        try:
            take_screenshot(data, i)
            print("berhasil disimpan")
        except Exception as e:
            print(e)

def main():
    file = './data/dataUrl.json'
    arrayUrl(file)
main()
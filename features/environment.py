from selenium import webdriver
import os

feature_dir = os.path.abspath(os.path.dirname(__file__))
chrome_driver_path = os.path.abspath(os.path.join(feature_dir, '..', 'node_modules', '.bin', 'chromedriver'))

def before_all(context):
    context.driver = webdriver.Chrome(chrome_driver_path)


def after_all(context):
    context.driver.quit()
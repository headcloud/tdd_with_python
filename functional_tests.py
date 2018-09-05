from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8324')

assert 'Django' in browser.title

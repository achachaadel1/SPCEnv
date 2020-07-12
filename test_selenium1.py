from selenium import webdriver
driver=webdriver.Chrome() #ouvrir Chrome
driver.get('http://10.70.201.42:9889/login.action?ssoLogin=true') #ouvrir l'url  Quotes.toscrape.com
CurrentURL = driver.current_url
nom_ut = driver.find_element_by_id('username')
nom_ut.send_keys('achach1')
mot_pas = driver.find_element_by_id('password')
mot_pas.send_keys('Adel1976')
login = driver.find_element_by_xpath('//*[@id="submitBtn"]/div/div')
login.click()
Client = driver.find_element_by_class_name('pluginbar_item_icon')
Client.click()


numeroClient = driver.find_element_by_id('serviceNo_input_value')
numeroClient.send_keys('36623011')

affi = str(input("clique sur OK pour voir l'url Actif  : "))
num = driver.find_element_by_name('searchCond.serviceNo')
num.send_keys('36623011')
num = driver.find_element_by_xpath('//*[@id="serviceNo_input_value"]')
num.send_keys('36623011')
num = driver.find_elements_by_css_selector('#serviceNo_input_value')
num.send_keys('36623011')

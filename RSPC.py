import time
v=int(input('Bonjour Mme Mr, pour travailler sur Internet tapez(1) ou pour NGBSS tapez (2): '))
if v==1:
    from selenium import webdriver
    driver=webdriver.Chrome() #ouvrir Chrome
    driver.get('https://facebook.com') #ouvrir l'url  https://facebook.com
    NomUt = input("Merci de saisie votre nom d'utilisateur :")
    Motpas = input("Merci de saisie votre mot de passe :")
    nom_ut = driver.find_element_by_id('email')
    nom_ut.send_keys(NomUt)
    mot_pas = driver.find_element_by_id('pass')
    mot_pas.send_keys(Motpas)
    login = driver.find_element_by_id('u_0_b')#trouver la touche connection
    login.click()
    time.sleep(5)  #arreté l'exection du programme pour 50 secondes

    #driver.close()  #fermer google chrome
elif v==2:
    from selenium import webdriver
    driver = webdriver.Chrome()  # ouvrir Chrome
    driver.get('http://10.70.201.42:9889/login.action?ssoLogin=true')  # ouvrir l'url  Quotes.toscrape.com
    time.sleep(5)
    CurrentURL = driver.current_url
    #if (CurrentURL) ==('http://10.70.201.42:9889/login.action?ssoLogin=true'):       nom_ut = driver.find_element_by_id('username')
    nom_ut.send_keys('achach1')
    mot_pas = driver.find_element_by_id('password')
    mot_pas.send_keys('Adel1976')
    login = driver.find_element_by_xpath('//*[@id="submitBtn"]/div/div')
    login.click()
    Client = driver.find_element_by_class_name('pluginbar_item_icon')
    Client.click()
    time.sleep(5)

    numeroClient = driver.find_element_by_id('serviceNo_input_value')
    numeroClient.send_keys('36623011')

else:
    print('vous avez taper un faut chiffre')
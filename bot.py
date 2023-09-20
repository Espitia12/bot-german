from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random

driver = webdriver.Chrome()

# Esperar para dar tiempo a que el navegador se inicie
# Ir a Instagram
sleep(2)
driver.get('https://www.instagram.com/accounts/login/')

sleep(5)

# Entrar
username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('nombre de usuario')
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('contraseña')
button_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
button_login.click()
sleep(5)
print('Sesión iniciada')

# Procesar hashtags
hashtag_list = ['gato', 'perro', 'ave']

for hashtag in hashtag_list:
    driver.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(6)

    first_thumbnail = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]/a/div[1]')
    first_thumbnail.click()
    sleep(50)

    for n in range(5): # Me gusta y comentario en el post n
        try:
            # Me gusta
            button_like = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div')
            button_like.click()
            sleep(random.randint(1,5))

            # Comentario
            reactions = ['😍', '😯', 'Wow!!']
            try:
                input_comment = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')
                input_comment.click()
            except:
                pass
            input_comment = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')
            input_comment.send_keys(random.choice(reactions))
            input_comment.send_keys(Keys.ENTER)
            sleep(random.randint(1,5))

            print('Post ' + str(n) + ' en #' + hashtag)

            # Ir al siguiente post
            button_next = driver.find_element(By.CSS_SELECTOR, '.coreSpriteRightPaginationArrow')
            button_next.click()
            sleep(random.randint(3,5))
        except Exception as e:
            print('Ocurrió una excepción:', str(e))
    print('#' + hashtag + ' completado')

# Cerrar el navegador al final
driver.quit()
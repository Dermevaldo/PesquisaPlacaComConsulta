from time import sleep

from PIL import Image, ImageFilter
import re
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

regex = r"[A-Z]{3}[0-9][0-9A-Z][0-9]{2}"
configt = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
nome_arquivo='teste.jpg'
placa_ori=Image.open(nome_arquivo)
placa_trabalhada=placa_ori.convert('L')
placa_trabalhada.save("copy.jpg")


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

texto = re.sub("\s",'',pytesseract.image_to_string(placa_trabalhada, lang='eng', config=configt))

print(texto)
texto=re.search(regex,texto)
texto=texto.group()
print(texto)
driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://apiplacas.com.br/consulta.php")
elem = driver.find_element(By.NAME, "placa")
elem.clear()

for letra in texto:
    elem.send_keys(letra)

elem.send_keys(Keys.RETURN)
driver.save_screenshot("resultado"+texto+".png")




print(texto)

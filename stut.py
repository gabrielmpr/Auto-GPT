from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path = "/Users/gabrielaguilarperez/Desktop/CS/Portfolio/gpt for browsers/chromedriver")
driver = uc.Chrome(service = service)

prompt = input("Insert your prompt for GPT: ")
mail = input("\nInsert your email: ")
password = input("\nInsert your password: ")


driver.get("https://chat.openai.com/")

time.sleep(3)

# WebDriverWait(driver, 5).until(
# 		EC.presence_of_element_located((By.CLASS_NAME, "relative flex h-12 items-center justify-center rounded-md text-center text-base font-medium bg-[#3C46FF] text-[#fff] hover:bg-[#0000FF]"))
# 	)

input_element  = driver.find_element(By.TAG_NAME, "button")
input_element.click()

time.sleep(3)

mail = driver.find_elements(By.TAG_NAME,"input")[1]
mail.send_keys(mail)

btn=driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

time.sleep(3)

password= driver.find_elements(By.TAG_NAME,"input")[2]
password.send_keys("13164444Beremiz")

time.sleep(3)

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_button-login-password")))
btn.click()

time.sleep(3)

inputElements = driver.find_elements(By.TAG_NAME, "textarea")

inputElements[0].send_keys(prompt)
time.sleep(2)
inputElements[0].send_keys(Keys.ENTER)
time.sleep(10)
inputElements = driver.find_elements(By.TAG_NAME, "p")
time.sleep(5)
results = []
for element in inputElements:
   results.append(element.text)

with open('gpt.txt', 'w') as file:
   for element in results:
      file.write(element)
print("You can find GPT's response in the text file")


# time.sleep(30)




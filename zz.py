# from selenium import webdriver 
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC 
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.common.by import By 

# # Initialize Chrome WebDriver
# driver = webdriver.Chrome()
# URL = 'https://web.whatsapp.com/' 
# driver.get(URL) 

# # Wait for the page to load
# wait = WebDriverWait(driver, 600) 

# # Define message parts
# string_message = "HELP! "
# url_link = "https://www.gps-coordinates.net/"
# message = string_message + url_link

# # Define target contact
# target_contact = "Saptarshi Majumder (IIITL|CSAI)"

# # Find the target contact and click on it
# user = driver.find_elements(By.XPATH,'//span[@title = "{}"]'.format(target_contact))
# user[0].click()

# # Find and click on the message input box
# msg_box = driver.find_element(By.XPATH,'//div[@title = "Type a message"]/div[2]')
# msg_box.click()

# # Send the message
# msg_box.send_keys(message + Keys.ENTER)

# # Print confirmation
# print("Message Sent")

s=''
s+='a\n'
s+='b\n'
print(s)
loc + whatsapp msg

# from selenium import webdriver 
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC 
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.common.by import By 
# import time
# import threading
# import datetime
# from bs4 import BeautifulSoup
# import requests
# import calendar as k

# from selenium import webdriver 
# driver = webdriver.Chrome()

# URL = 'https://web.whatsapp.com/' 
# driver.get(URL) 

        # geo_request = requests.get(url)
        # import requests
        # r = requests.get('https://get.geojs.io/')
        # ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        # loc = []
        # ipAdd = ip_request.json() ['ip']
        # loc.append(ipAdd)
        # url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        # geo_request = requests.get(url)
        # geo_data = geo_request.json()
        # # print(geo_data)
        # loc.append(geo_data['latitude'])
        # loc.append(geo_data['longitude'])
        # loc.append(geo_data['city'])
        # loc.append(geo_data['region'])
        # loc.append(geo_data['country'])
        # loc.append(geo_data['timezone'])
        
        # s=""
        # for i in loc:
        #     s+=str(i)+" "
        # print(s)
            
        
        # wait = WebDriverWait(driver, 600) 
        # string = s
        # target = "Saptarshi Majumder (IIITL|CSAI)"
        # user = driver.find_elements(By.XPATH,'//span[@title = "{}"]'.format(target))
        # user[0].click()
        # msg_box = driver.find_element(By.XPATH,'//div[@title = "Type a message"]/p')
        # msg_box.click()
        # msg_box.send_keys(string+Keys.ENTER)
        # print("msg_Sent")
        
        
        
# sound


# import winsound

# # Set frequency to 2000 Hertz
# frequency = 10000

# # Set duration to 1500 milliseconds (1.5 seconds)
# duration = 5000

# # Make beep sound on Windows

# winsound.Beep(frequency,duration)
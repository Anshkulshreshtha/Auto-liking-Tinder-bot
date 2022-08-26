from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

email = "anshkulshreshtha01@gmail.com"
password = "09876poiuy"

chrome_driver_path = "c:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

sleep(2)
driver.get("https://tinder.com/")

#turning off the cookies--
cookies_off = driver.find_element(By.XPATH,'//*[@id="o-1389276889"]/div/div[2]/div/div/div[1]/div[2]/button')
if(cookies_off):
    cookies_off.click()

#----------------------------Login part----

sleep(5)
Login_button = driver.find_element(By.XPATH,"//*[text()='Log in']")
Login_button.click()

# more_options_to_log = driver.find_element(By.CLASS_NAME, "Td(u).Cur(p).Fw($medium).Tt(u)--ml focus-outline-style")
# if(more_options_to_log):
#     more_options_to_log.click()

sleep(5)
Facebook_button = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button")
Facebook_button.click()

#-----Shifting to a new windwow-----
sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)     #for the verification that we are on a correct window i.e.  Facebook

Email = driver.find_element(By.ID,"email")
Password = driver.find_element(By.ID, "pass")

Email.send_keys(email)
Password.send_keys(password)

Password.send_keys(Keys.ENTER)  #hitting enter after password

#-----revert back to the base window & verify the window via printing title
driver.switch_to.window(base_window)
print(driver.title)

#---Giving the permission for the location access----
sleep(5)
#Allow location
allow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="o1177309331"]/main/div/div/div/div[3]/button[2]/span')
notifications_button.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()


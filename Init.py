from selenium import webdriver
import Filtering_Connections


def Linkedin_signIn():
    website_link = "https://www.linkedin.com/m/login"
    browser = webdriver.Firefox()
    browser.get((website_link))
    #Please edit email and password or else program runs into errors
    email = "*****Your Email Here*****"
    pass_word = "*****Your Password Here*****"

    element_for_username = "session_key"
    element_for_password = "session_password"
    element_for_submit = "button"

    browser.switch_to_frame(
        browser.find_element_by_class_name("authentication-iframe"))
    signIn_link = browser.find_element_by_link_text("Sign in")
    signIn_link.click()

    username = browser.find_element_by_name(element_for_username)
    username.send_keys(email)
    password = browser.find_element_by_name(element_for_password)
    password.send_keys(pass_word)


    signInButton = browser.find_element_by_tag_name(element_for_submit)
    signInButton.click()
    Filtering_Connections.My_Network(browser)

i = 0
while i!=10:

    Linkedin_signIn()
    i+=1
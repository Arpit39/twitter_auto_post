
# 


import os
from django.shortcuts import render 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager

# Create your views here.

# path="/usr/bin/google-chrome /usr/share/man/man1/google-chrome.1.gz"
# driver=webdriver.Chrome(path)
# driver = webdriver.Chrome('/path/to/chromedriver') 
# driver = webdriver.Chrome(executable_path='/usr/bin/google-chrome /usr/share/man/man1/google-chrome.1.gz')


def index(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        post=request.POST.get("post")
        ############
        try:
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            linkedin_home_page="https://twitter.com/"
            driver.get(linkedin_home_page)
            driver.implicitly_wait(3)
            driver.maximize_window()
            sigin_in=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/a")
            print(sigin_in,"#####################")
            sigin_in.click()
        except:
            pass

        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get(login_url)
        # input_username=driver.find_element_by_tag_name("input")
        # Button=driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]")
        # input_username.send_keys(username)
       
        # Button.click()
        # input_password=driver.find_element_by_name("password")
       
        # input_password.send_keys(password)
        
    
    return render(request,"index.html")
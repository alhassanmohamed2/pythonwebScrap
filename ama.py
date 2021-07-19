#CopyRigths Alhassan Mohamed HaHaHa
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import csv
import time
No_PlPPpage = 5 #This number is the count of how many PLPPage Div in the page as they increasing byy scrolling
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

url = 'https://en-ae.6thstreet.com/men/clothing/t-shirts.html'
driver.get(url)
time.sleep(10)
while True:
    tt = driver.execute_script('var tt; window.scrollBy(0,1000); window.scrollBy(0,-200);   tt =document.querySelectorAll("div.PLPPage").length;return tt;')
    if tt == No_PlPPpage:
        break
    time.sleep(5)
html = driver.execute_script('var imgs = [];var no_imgs = document.querySelectorAll("div.PLPPage .ProductItem img").length;for(i=0;i<no_imgs;i++){imgs[i]=document.querySelectorAll("div.PLPPage .ProductItem img")[i].getAttribute("src")}return imgs;')
for i in range(len(html)):
    print(html[i])




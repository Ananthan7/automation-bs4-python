from selenium import webdriver
import time

#add driver path
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')
browser.get('https://google.com')
#sleep time for some seconds 
time.sleep(1)
#find x-path of search button and send keys to it
search_input = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_input.send_keys('wikipedia')

#search button is clicked
search_button = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
search_button.click() 


search_name = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3/span')
search_name.click() 

result =browser.find_element_by_xpath(' //*[@id="mw-content-text"]/div[1]/p[2]')

print( 'result:'+ result.text)
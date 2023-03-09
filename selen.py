#! /usr/bin/env python3 

from  selenium import webdriver 
from selenium.webdriver.common.by import By 

type_video = "&sp=CAMSAhAB"
type_playlist = "&sp=EgIQAw%253D%253D"


def video_scraping(url) : 
    # in linux the default path is in /usr/local/bin 
    # if os is different then u should installthe web driver and pass the path  of the webdriver as parameter for Chrome method of webdriver class 
    driver = webdriver.Chrome()

    driver.get(targeted_website) # to go into this page and open it into the chrome browser .  

    # le xpath est un language utilise pou localiser une portion d'un document xml  . 
    # find the filter button and click on this.button  in order to show the list 
    button_filter = driver.find_element(By.XPATH ,'//*[@id="container"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
    button_filter.click()
    

    type_data = driver.find_element(By.XPATH , '//*[@id="collapse-content"]/ytd-search-filter-group-renderer[2]/ytd-search-filter-renderer[1]')

    type_data.click()

    views = driver.find_elements(By.XPATH , '//*[@id="metadata-line"]/span[1]')
    pure_views = []
    for i in views :
        pure_views.append(i.text)
      


    video_title = driver.find_elements(By.XPATH , '//*[@id="video-title"]/yt-formatted-string')
    
    pure_vid_title = []
    for  i in video_title :
        pure_vid_title.append(i.text)
      

    list_of_data = list(zip(pure_views, pure_vid_title))
    print(f"- The best 4 videos to learn {key_word} from youtube are : ")
    for  i in range(0,3) : 
        print(f"\n - video title : {list_of_data[i][1]} ||  numberOfVues : {list_of_data[i][0]}\n")
    driver.quit() 



def playlist_scraping(url) :
    driver = webdriver.Chrome()
    targeted_website = f"https://www.youtube.com/results?search_query={key_word}{type_playlist}"
    driver.get(targeted_website)

    button_filter =driver.find_element(By.XPATH ,'//*[@id="container"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
    button_filter.click()

    type_data = driver.find_element(By.XPATH , '//*[@id="label"]/yt-formatted-string')
    type_data.click()

    channel = driver.find_elements(By.XPATH , '//*[@id="text"]/a')
    x = []
    for i in channel :
        x.append(i.text)

    title= driver.find_elements(By.XPATH ,'//*[@id="video-title"]' )
    titre = []
    for i in title:
        titre.append(i.text)

    list_of_data = list(zip(x,titre))


    print(f"- The best 4 playlists to learn {key_word} from youtube are : ")
    for  i in range(0,4) :
            print(f" - playlist title : {list_of_data[i][1]} \n - channel : {list_of_data[i][0]} \n")


    

setState = True 
while (setState == True ) : 
    key_word = input("- Enter what u want to lean from youtube : ") # the key word that the user will enter in order  to scarpe the data for 
    type_wanted = int(input("- Playlist/video  [1/0]: ")) 

    if (type_wanted == 1 ) :
        print(" - you choose playlist type  :  ")
        targeted_website = f"https://www.youtube.com/results?search_query={key_word}{type_playlist}"
        playlist_scraping(targeted_website)

    else : 
        print(" - you choose videos  :  ")
        targeted_website = f"https://www.youtube.com/results?search_query={key_word}{type_video}"
        video_scraping(targeted_website)
    
    x = str(input("- Any other help for your learning : [y/n]")).strip()
    if (x == 'y' ) : 
        setState = True
    else : 
        setState = False 
        print("- Bye !")

# to quit the webdriver that we have opened . 



# tuto : 
# to send some information such as input data to login or to sign up we should import first  keys from 
# common webdriver selenium using the next syntax : from selenium.webdriver.Keys import Keys 
# to send data from localhost to the server : 
# webdriver.Chrome().find_element(By.XPATH , "parse here the xpath of the input").send_keys('here parse the data') 
# driver.quit() : to quit the webdriver . 
# .text to get  the text of the selected item . 
# .implicitly_wait(time) : to wait a certain number of time until a certain command is estabished . 
# The zip function iterates over several iterables in parallel and produces tuples with an item from each iterable.




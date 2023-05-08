from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
from sendmail import send_email

# link to youtube trending page
YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'


def get_driver():
    # path to chrome driver on my pc
    driver = webdriver.Chrome(r'C:\Windows\chromedriver.exe')
    return driver
    
def get_videos(driver):
    driver.get(YOUTUBE_TRENDING_URL)
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
    return videos


def parse_video(video): 
    """title , url, thumbmail, channel, view
      uploaded, description"""

    # title
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text

    # url source
    url = title_tag.get_attribute('href')

    # thumbmail
    thumbmail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbmail_url = thumbmail_tag.get_attribute('src')
    
    # channel name
    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_div.text

    # description
    description = video.find_element(By.ID, 'description-text').text

    # duration

    # view

    # uploaded

    return{
        'title':title,
        'url': url,
        'thumbmail_url': thumbmail_url,
        'channel_name': channel_name,
        'description': description
    }

if __name__ == "__main__":
    print('Create driver')
    driver = get_driver()

    print("Fetching the page")
    videos = get_videos(driver)
     
    print(f'Found {len(videos)} videos')


    print('parsing top tending videos')
    video_data = [parse_video(video) for video in videos]
    print(video_data)


    print('save the data as csv')
    video_df = pd.DataFrame(video_data)
    print(video_df)

    # video_df.to_csv('top trending youtube videos.csv', index=False)



    # print('page title:', driver.title)

    print("send an email")
    body = json.dumps(video_data, indent = 2)
    send_email(body)
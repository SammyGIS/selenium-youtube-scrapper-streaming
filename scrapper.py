import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

response = requests.get(YOUTUBE_TRENDING_URL)

# print(response.status_code)


try:
    with open('trending.html', 'wb') as f:
        f.write(response.text.encode('cp1252'))

except UnicodeEncodeError:
    with open('trending.html', 'wb') as f:
        f.write(response.text.encode('cp1252', errors='ignore'))


# print the first 1000 text
# print(response.text[:1000])


doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title.text)


# find all the video divson the website
video_divs = doc.find_all('div', class_ = "ytd-video-renderer")

print(f'Found {len(video_divs)} videos')



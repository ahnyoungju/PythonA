import requests
from bs4 import BeautifulSoup
#import urllib.request

def print_headlines(response_text):
  soup = BeautifulSoup(response_text, features = 'lxml')
  #headlines = soup.find_all(attrs={"class" : "VDXFz"})

  headlines = soup.find_all('a', href = True)[25:-50]
  #print(headlines)

  outF = open("myOutFile.txt", "w")

  for headline in headlines:
    print(headline.text)
    outF.write(headline.text)
    outF.write("\n")

  outF.close()



# url = 'https://au.news.yahoo.com'
url = 'https://www.msn.com/en-au/news'
response = requests.get(url)
print_headlines(response.text)
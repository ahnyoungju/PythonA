from bs4 import BeautifulSoup as soup    #Beautiful Soup is a Python library for pulling data out of HTML or XML files.

from urllib.request import urlopen          #urllib.request is a Python module for fetching URLs.It offers a very
                                            #simple interface, in the form of the urlopen function.

import json                                     #The JSON module is mainly used to convert the python dictionary
                                                # into a JSON string


news_url = "https://news.google.com/news/rss"   #news link to web scrap for tiltes, URL link and pubDate
d_client = urlopen(news_url)                      #urllib is a python module that fectes the url link with urlopen
xml_page = d_client.read()                          #read method read the opened url page and stores in the variable
d_client.close()                                      #after the file, client closed the connection with clinet() method

soup_page = soup(xml_page, "xml")               #Beautiful 'Soup' is a library used for scrapping web pages.
                                                # It sits atop an HTML or XML parser, providing Pythonic idioms
                                                #for iterating, searching, and modifying the parse tree.

news_list = soup_page.findAll("item")           #Passing a string to a search method and Beautiful Soup and from the
                                                #read URL page find all HTML tags "item" from tree and store in new_list


extracted_records = []                          #want to prepend that information which is relevant, build a dictionary
                                                #with a for loop which will find titles,links and publication date.

for news in news_list:                          #for loop which will iterate over news_list for title, links and pubDate
                                                #and store the information in the variable news.
    title = news.title
    links = news.links
    pubDate = news.pubDate

    records = {
        'title'     :news.title.text,
        'links'     :news.link.text,
        'pubDate'   : news.pubDate.text,
         }

    extracted_records.append(records)           #lets append all the clean data in dictionary as items
    #print(extracted_records)

    with open('NewsData.json', 'w') as outfile:             #Now use a JSON serializer and save this data into a JSON
                                                            # file. The code below creates and opens a file called
                                                            # NewsData.json and writes the data into it.

        json.dump(extracted_records, outfile, indent=2)        #converting python dictionary into json boject

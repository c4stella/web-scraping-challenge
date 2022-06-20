import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url_news = 'https://redplanetscience.com/'
    url_imgs = 'https://spaceimages-mars.com'
    url_info = 'https://galaxyfacts-mars.com'
    url_hemi = 'https://marshemispheres.com/'

    browser.visit(url_news)

    html_news = browser.html
    soup_news = bs(html_news,'html.parser')
    article = soup_news.find('div', class_='list_text')

    news_title = article.find('div', class_='content_title').text
    print(news_title)
    news_text = article.find('div', class_='article_teaser_body').text
    print(news_text)

    #rest of script
    #returns python dict with all results
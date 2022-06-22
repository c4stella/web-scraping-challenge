import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Setting up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URLs to scrape
    url_news = 'https://redplanetscience.com/'
    url_imgs = 'https://spaceimages-mars.com'
    url_info = 'https://galaxyfacts-mars.com'
    url_hemi = 'https://marshemispheres.com/'

    # Visit redplanetscience
    browser.visit(url_news)

    # Scrape page using beautifulsoup
    html_news = browser.html
    soup_news = bs(html_news,'html.parser')
    article = soup_news.find('div', class_='list_text')

    # Get featured article title and text
    news_title = article.find('div', class_='content_title').text
    news_text = article.find('div', class_='article_teaser_body').text


    # Visit spaceimages
    browser.visit(url_imgs)

    # Scrape page using beautifulsoup
    html_imgs = browser.html
    soup_imgs = bs(html_imgs, 'html.parser')
    image = soup_imgs.find('img', class_='headerimage fade-in')

    # Get image url of featured image
    featured_image_url = url_imgs + '/' + image['src']


    # Read in html table from page using pandas
    html_info = pd.read_html(url_info)

    # Iterate through list of table data
    html_str_info = []

    for tab in html_info:
        # Render tables as html strings, append to empty list
        html_str = tab.to_html()
        html_str_info.append(html_str)


    # Visit marshemispheres
    browser.visit(url_hemi)

    # Scrape page using beautifulsoup
    html_hemi = browser.html
    soup_hemi = bs(html_hemi, 'html.parser')
    hemispheres = soup_hemi.find_all('img', class_='thumb')

    # Iterate through list of results to find image data
    hemisphere_image_urls = []

    for h in hemispheres:
        # Save name of image
        img_alt = h['alt']
        hem_name = img_alt.replace(' Enhanced thumbnail','')

        # Save and edit image url
        img_src = h['src']
        hem_img = url_hemi + img_src.replace('_thumb.png','')

        # Save name and image url as a key:value pair
        hem_dict = {'title': hem_name, 'img_url': hem_img}

        # Append dictionaries to empty list
        hemisphere_image_urls.append(hem_dict)


    # Store results
    mars_data = {
        'news_title': news_title,
        'news_text': news_text,
        'featured_image_url': featured_image_url,
        'table_str': html_str_info,
        'hemispheres': hemisphere_image_urls
    }
    
    browser.quit()

    return mars_data
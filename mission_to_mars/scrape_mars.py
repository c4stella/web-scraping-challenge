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

    # Using redplanetscience ----------------------------------------------------------
    browser.visit(url_news)

    # Scrape page using beautifulsoup
    html_news = browser.html
    soup_news = bs(html_news,'html.parser')
    article = soup_news.find('div', class_='list_text')

    # Get featured article title and text
    news_title = article.find('div', class_='content_title').text
    news_text = article.find('div', class_='article_teaser_body').text
    # ---------------------------------------------------------------------------------


    # Visit spaceimages ---------------------------------------------------------------
    browser.visit(url_imgs)

    # Scrape page using beautifulsoup
    html_imgs = browser.html
    soup_imgs = bs(html_imgs, 'html.parser')
    image = soup_imgs.find('img', class_='headerimage fade-in')

    # Get image url of featured image
    featured_image_url = url_imgs + '/' + image['src']
    # ---------------------------------------------------------------------------------


    # Scraping tablular data with pandas ----------------------------------------------
    html_info = pd.read_html(url_info)

    # Saving html string to variable
    table_str = html_info[0].to_html(classes='table')
    # ---------------------------------------------------------------------------------


    # Visit marshemispheres -----------------------------------------------------------
    browser.visit(url_hemi)

    # Scrape page using beautifulsoup
    html_hemi = browser.html
    soup_hemi = bs(html_hemi, 'html.parser')
    hemispheres = soup_hemi.find_all('div', class_='description')

    # Empty lists for iteration
    hem_title = []
    hemisphere_pages = []

    # Iterate through list of results to find image data
    for h in hemispheres:
        
        # Save name of image
        img_name = h.find('h3')
        hem_name = img_name.text
        hem_title.append(hem_name)

        # Save urls of each hemisphere page, to visit later for full images
        hemlink = h.find('a')
        hemurl = url_hemi + hemlink['href']
        hemisphere_pages.append(hemurl)

    # Empty list for iteration
    hem_img_urls = []

    # Iterate through list of urls to find full images
    for p in hemisphere_pages:

        # Visit url specified
        browser.visit(p)

        # Setting up html and soup
        current_html = browser.html
        current_soup = bs(current_html, 'html.parser')

        # Find object with image, extract its link
        hem_img = current_soup.find('img', class_='wide-image')
        hem_img_url = url_hemi + hem_img['src']

        # Save image url
        hem_img_urls.append(hem_img_url)
    
    # Empty list for iteration
    hem = []

    # Iterate through lists of titles and urls, with 4 items each
    for i in range(4):

        # Save name and image url as a key:value pair
        hem_dict = {'title': hem_title[i - 1], 'img_url': hem_img_urls[i - 1]}
        hem.append(hem_dict)
    # ---------------------------------------------------------------------------------

    # Store results -------------------------------------------------------------------
    mars_data = {
        'news_title': news_title,
        'news_text': news_text,
        'featured_image_url': featured_image_url,
        'table_str': table_str,
        'hemispheres': hem
    }
    
    browser.quit()

    return mars_data
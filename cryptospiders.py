from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup as bs
import json
import time
import re

from library.splittext import splitText


# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False

# %%


class Crawlers(object):

    LOADING_PAGE = time.sleep(15)

    def __init__(self, filename='web_crawl_output.json'):
        self.filename = filename

    # ------------------- COINBUREAU

    def coinbureau(self):
        """Crawl the coinbureau blog 'https://www.coinbureau.com/blog/'

        Returns:
            list: filename, column headers and data fetched by the crawler
        """
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.coinbureau.com/blog/')
            driver.maximize_window()
            # scroll upto 5 times
            time.sleep(5)
            browse_content_gif = driver.find_element(
                by=By.CLASS_NAME, value='feed__load-more-button')
            for i in range(0, 5):
                # there are upto 5 lazy-loading instances before gif-image deactivates functionality
                time.sleep(10)
                driver.execute_script("arguments[0].scrollIntoView()", browse_content_gif)

            Crawlers.LOADING_PAGE
            html_content = bs(driver.page_source, 'lxml')
            favourite="bitcoin"
            documents = []
            postid = 0
            for tag in html_content.find_all('div', class_='feed__post'):
                
                linesDict = {'bitcoin': 0, 'ethereum': 0, 'xrp': 0, 'tether': 0, 'cardano': 0, 'polkadot': 0,\
                            'stellar': 0, 'usdt': 0, 'dogecoin': 0, 'doge': 0,'chainlink': 0, 'crypto':0, 'nft':0, 'avax':0, 'sol':0}
                
                max_linesDict = {'bitcoin': 0, 'ethereum': 0, 'xrp': 0, 'tether': 0, 'cardano': 0, 'polkadot': 0,\
                            'stellar': 0, 'usdt': 0, 'dogecoin': 0, 'doge': 0,'chainlink': 0, 'nft':0, 'avax':0, 'sol':0}
                
                
                cp =splitText()
                
                # core data
                date = tag.find('span', class_='feed__date').text.strip().replace("\n", " ")
                title = tag.find('h3', class_='feed__title').text.strip().replace("\n", " ")
                title_encode = title.encode("ascii", "ignore")
                title = title_encode.decode()
                url = tag.find('a', class_="feed__clickable")[
                    'href'].strip().replace("\n", " ")
                if url is not None:
                    article = ""
                    try:
                        driver.get(url)
                        tree = bs(driver.page_source, 'lxml')
                        article_content = tree.find(
                            'div', attrs={'class': re.compile("^article single__content")})
                        for para in article_content('p'):
                            favourite="bitcoin"
                            for _ in para('a'):
                                _.decompose()
                            article = article+ " " + para.text.strip().replace("\n", " ")
                            
                            article_encode = article.encode("ascii", "ignore")
                            article = article_encode.decode()
                            article_lower = article.lower()
                            for key in linesDict:
                                if(key in article_lower):
                                    if(linesDict[key] != 1):
                                        linesDict[key] += 1
                                        
                            for key in max_linesDict:
                                if(key in article_lower):
                                        max_linesDict[key] += 1
                                        
                            for key in max_linesDict:
                                if(max_linesDict[key] >= max_linesDict[favourite]):
                                    favourite=str(key)
                            
                    except:
                        pass
                else:
                    article = "NIL"
                doc = {'postid': postid, 'date': date,
                        'title': title, 'url': url, 'article': article, "outlet": "coinbureau", "author": "coinbureau", "favourite":favourite, "polarity":cp.get_polarity(title)} 
                # metadata
                readtime = tag.find(
                    'span', class_="feed__read-time").text.strip().replace("\n", " ")
                category = tag.find(
                    'ul', class_="post-categories").text.strip().replace("\n", " ")
                
                # author = tag.find('span', class_="author__link")
                # print(author)
                
                metadata = {"source": "coinbureau", "readtime": readtime, "category": category}
                doc.update({'metadata': metadata, "category": category, \
                    'bitcoin': linesDict['bitcoin'], 'ethereum': linesDict['ethereum'], 'xrp': linesDict['xrp'], 'tether': linesDict['tether'], 'cardano': linesDict['cardano'], 'polkadot': linesDict['polkadot'],\
                    'stellar': linesDict['stellar'], 'usdt': linesDict['usdt'], 'dogecoin': linesDict['dogecoin'], 'doge': linesDict['doge'], 'chainlink': linesDict['chainlink'], 'avax':linesDict['avax'], \
                        'sol':linesDict['sol'], 'nft':linesDict['nft'], 'crypto':linesDict['crypto']})
                documents.append(doc)
                postid += 1

            driver.quit()
            return (self.filename, json.dumps(documents, indent=4))
        except Exception as e:
            print(f'\nPage could not be processed\n\n{e}')
        return None

    # ------------------- FORBES

    def forbes(self):
        """crawl the forbes website blog by billy banbrough: 'https://www.forbes.com/sites/billybambrough/?sh=28b3aa666a89'

        Returns:
            list: filename, column headers and data fetched by the crawler
        """
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.forbes.com/sites/billybambrough/?sh=28b3aa666a89')
            driver.maximize_window()
            time.sleep(15)

            for _ in range(0, 5):
                # with checking, there are upto 4 page-loads before the button disappears
                driver.find_element(by=By.CLASS_NAME, value='load-more').click()

            Crawlers.LOADING_PAGE
            html_content = bs(driver.page_source, 'lxml')
            favourite="bitcoin"
            documents = []
            postid = 0
            for tag in html_content.find_all('div', class_="stream-item__text"):
                linesDict = {'bitcoin': 0, 'ethereum': 0, 'xrp': 0, 'tether': 0, 'cardano': 0, 'polkadot': 0,\
                            'stellar': 0, 'usdt': 0, 'dogecoin': 0, 'doge': 0,'chainlink': 0, 'crypto':0, 'nft':0, 'avax':0, 'sol':0}
                max_linesDict = {'bitcoin': 0, 'ethereum': 0, 'xrp': 0, 'tether': 0, 'cardano': 0, 'polkadot': 0,\
                            'stellar': 0, 'usdt': 0, 'dogecoin': 0, 'doge': 0,'chainlink': 0, 'nft':0, 'avax':0, 'sol':0}
                
                
                cp =splitText()
                date = tag.find('div', class_='stream-item__date').text.strip()
                if(str(datetime.now().year) not in date):
                    date = datetime.now().strftime("%b %d, %Y")
                    
                title = tag.find('a', class_='stream-item__title').text.strip()
                title_encode = title.encode("ascii", "ignore")
                title = title_encode.decode()
                url = tag.find('a', class_='stream-item__title')['href'].strip()
                if url is not None:
                    article = ""
                    try:
                        driver.get(url)
                        tree = bs(driver.page_source, 'lxml')
                        article_content = tree.find(
                            'div', attrs={'class': re.compile("^article-body fs-article")})
                        for para in article_content('p'):
                            for _ in para('a'):
                                _.decompose()
                            for _ in para('strong'):
                                _.decompose()
                            article = article + " " + para.text.strip().replace("\n", " ").replace("\"", " ").replace("\u2014", " ")
                            article_encode = article.encode("ascii", "ignore")
                            article = article_encode.decode()
                            article_lower = article.lower()
                            for key in linesDict:
                                if(key in article_lower):
                                    if(linesDict[key] != 1):
                                        linesDict[key] += 1
                                        
                            for key in max_linesDict:
                                if(key in article_lower):
                                        max_linesDict[key] += 1
                                        
                            for key in max_linesDict:
                                if(max_linesDict[key] >= max_linesDict[favourite]):
                                    favourite=str(key)
                                    
                    except:
                        pass
                else:
                    article = "NIL"
                doc = {'postid': postid, 'date': date,
                       'title': title, 'url': url, 'article': article, "outlet": "forbes", "favourite":favourite, "polarity":cp.get_polarity(title)}
                # metadata
                views = tag.find('div', class_='stream-item__views').text.split("views")[0].strip()
                summary = tag.find('div', class_='stream-item__description').text.strip()
                metadata = {"source": "forbes", "author": "Billy Bambrough",
                            "views": views, "summary": summary}
                doc.update({'metadata': metadata, "author": "Billy Bambrough", "views": views, "summary": summary, \
                    'bitcoin': linesDict['bitcoin'], 'ethereum': linesDict['ethereum'], 'xrp': linesDict['xrp'], 'tether': linesDict['tether'], 'cardano': linesDict['cardano'], 'polkadot': linesDict['polkadot'],\
                    'stellar': linesDict['stellar'], 'usdt': linesDict['usdt'], 'dogecoin': linesDict['dogecoin'], 'doge': linesDict['doge'], 
                    'chainlink': linesDict['chainlink'], 'avax':linesDict['avax'], 'sol':linesDict['sol'], 'nft':linesDict['nft'], 'crypto':linesDict['crypto']})
                documents.append(doc)
                postid += 1

            driver.quit()
            return (self.filename, json.dumps(documents, indent=4))
        except Exception as e:
            print(f'\nPage could not be processed\n\n{e}')
        return None

    # ------------------- MONEYWEB

    def moneyweb(self):
        """Crawl the moneyweb website: 'https://www.moneyweb.co.za/moneyweb-crypto/'

        Returns:
            list: filename, column headers and data fetched by the crawler
        """
        driver = webdriver.Chrome()
        driver.get('https://www.moneyweb.co.za/moneyweb-crypto/')
        Crawlers.LOADING_PAGE
        html_content = bs(driver.page_source, 'lxml')
        favourite="bitcoin"
        documents = []
        postid = 1
        try:
            for tag in html_content.\
                    find_all('div', class_='col-lg-8 col-md-8 col-sm-8 col-xs-8 clear-padding-right'):

                linesDict = {'bitcoin': 0, 'ethereum': 0, 'xrp': 0, 'tether': 0, 'cardano': 0, 'polkadot': 0,\
                            'stellar': 0, 'usdt': 0, 'dogecoin': 0, 'doge': 0,'chainlink': 0, 'crypto':0, 'nft':0 , 'avax':0, 'sol':0}
                
                max_linesDict = {'bitcoin': 0, 'ethereum': 0, 'xrp': 0, 'tether': 0, 'cardano': 0, 'polkadot': 0,\
                            'stellar': 0, 'usdt': 0, 'dogecoin': 0, 'doge': 0,'chainlink': 0, 'nft':0, 'avax':0, 'sol':0}
                
                
                cp =splitText()
                
                _ = tag.find('div', class_="grey-text inline-block")
                date = _.find('span', "inline-block").text.replace('/', "").strip()
                title = tag.find('h3', class_='title list-title m0005').text.strip()
                title_encode = title.encode("ascii", "ignore")
                title = title_encode.decode()
                _ = tag.find('h3', class_="title list-title m0005")
                url = _.find('a')['href'].strip()
                if url is not None:
                    article = ""
                    
                    try:
                        driver.get(url)
                        tree = bs(driver.page_source, 'lxml')
                        article_content = tree.find('div', attrs={'class': "article-content"})
                        for para in article_content('p'):
                            for _ in para('a'):
                                _.decompose()
                            for _ in para('strong'):
                                _.decompose()
                            article = article + " " + para.text.strip().replace("\n", " ")
                            article_encode = article.encode("ascii", "ignore")
                            article = article_encode.decode()
                            article_lower = article.lower()
                            for key in linesDict:
                                if(key in article_lower):
                                    if(linesDict[key] != 1):
                                        linesDict[key] += 1
                                        
                            for key in max_linesDict:
                                if(key in article_lower):
                                        max_linesDict[key] += 1
                                        
                            for key in max_linesDict:
                                if(max_linesDict[key] >= max_linesDict[favourite]):
                                    favourite=str(key)
                                
                    except:
                        pass
                else:
                    article = "NIL"
                doc = {'postid': postid, 'date': date,
                        'title': title, 'url': url, 'article': article, "outlet": "moneyweb", "favourite":favourite, "polarity":cp.get_polarity(title)}
                # metadata
                summary = tag.find('div', class_="excerpt m0010").text.strip()
                category = tag.find('div', class_="inline-block m0005 m05right hidden-xs")
                if category is None:
                    category = "Sponsored content"
                else:
                    category = category.text.strip()
                author = tag.find('span', class_="mny-light-blue").text.strip()
                metadata = {"source": "moneyweb", "author": author,
                            "category": category, "summary": summary}
                doc.update({'metadata': metadata, "author": author, "category": category, "summary": summary, \
                    'bitcoin': linesDict['bitcoin'], 'ethereum': linesDict['ethereum'], 'xrp': linesDict['xrp'], 'tether': linesDict['tether'], 'cardano': linesDict['cardano'], 'polkadot': linesDict['polkadot'],\
                    'stellar': linesDict['stellar'], 'usdt': linesDict['usdt'], 'dogecoin': linesDict['dogecoin'], 
                    'doge': linesDict['doge'], 'chainlink': linesDict['chainlink'], 'avax':linesDict['avax'], 'sol':linesDict['sol'], 'nft':linesDict['nft'], 'crypto':linesDict['crypto']})
                documents.append(doc)
                postid += 1

            driver.quit()
            return (self.filename, json.dumps(documents, indent=4))
        except Exception as e:
            print(f'\nPage could not be processed\n\n{e}')
        return None
    
    
# cp = Crawlers()
# cp.moneyweb()
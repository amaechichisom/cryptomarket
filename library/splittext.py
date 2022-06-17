import pandas as pd
import nltk
import re
from textblob import TextBlob
from datetime import datetime
from pyspark.sql import SparkSession, types
from pyspark.sql import udf, functions as func


class splitText:
    """(class) splitext splits a given text form a file or string input using regular expressions
    if the key are given otherwise returns all the works
    """
    
    #default constructor
    def __init__(self):
        pass
            
    #get text, splits it
    def splitWithRe(self,spark,keys=[]):
        """splitWithRe(text,keys=[]), text mandetory, keys optional. if keys are not supplied,
        word count will be done to all the words.
        """
        #create spark sessiion 
        # spark = SparkSession.builder.appName("DataCleanse").getOrCreate()
        lines = spark.readStream.format('socket').option("host", "localhost").option("port", 9999).load()
        pandasDF = pd.DataFrame(lines)
        data = spark.createDataFrame(pandasDF.astype(str))
        # Split using a regular expression that extracts words
        words = lines.select(func.explode(func.split(func.lower(data[0]), "\\W+")).alias("word"))
        if keys == []:
            words.filter(words.word != "")
        else:
            words.filter(words.word.isin(keys))

        wordCount = words.select('word').groupBy('word').agg(func.count('word').alias('count'))
           
        return wordCount.collect()
    
    def get_mentions(self,text):
        """ gets words list and their cout=1? and returns the mentions( i.e. #-tags) as a list"""
        words = text.split()
        mentions = [mention.strip('#') for mention in words if mention.startswith('#')]
              
        return mentions
    
    def contains_word(self, s, w):
        return f' {w} ' in f' {s} '

    def get_polarity(self,text):
        """get_polarity(self,text) get content as text, clean it and analyze its poplarity."""

        clean_txt = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
        
        analysis = TextBlob(clean_txt)
        
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"
    
    def get_replies(self,text):
        """get_replies(self,text) get a text and returns dict of replies and the count"""


#correct dates
class dates():
    """"""
    def monthInt(self,val):
        if val == 'jan': return str(1).zfill(2)
        if val == 'feb': return str(2).zfill(2)
        if val == 'mar': return str(3).zfill(2)
        if val == 'apr': return str(4).zfill(2)
        if val == 'may': return str(5).zfill(2)
        if val == 'jun': return str(6).zfill(2)
        if val == 'jul': return str(7).zfill(2)
        if val == 'aug': return str(8).zfill(2)
        if val == 'sep': return str(9).zfill(2)
        if val == 'oct': return str(10)
        if val == 'nov': return str(11)
        if val == 'dec': return str(12)

    def correctDate(self,row):
        now = datetime.now()          
        if row[5] == 'coinbureau' or row[5] == 'moneyweb':
            if row[1].__contains__('ago'):
                date = '{0}-{1}-{2}'.format(str(now.year).zfill(4),str(now.month).zfill(2),str(now.day).zfill(2))
            else:
                dt_raw = row[1].split()
                date = dt_raw[0]

        if row[5] =='forbes':   
            if row[1].__contains__('ago'):
                date = '{0}-{1}-{2}'.format(str(now.year).zfill(4),str(now.month).zfill(2),str(now.day).zfill(2))
            else:
                dt_raw = row[1].split(', ') 
                yr, mmmdd = dt_raw[1], dt_raw[0].split()
                mnth, dd = self.monthInt(mmmdd[0].lower()),mmmdd[1].zfill(2)
                date = '{0}-{1}-{2}'.format(yr,mnth,dd)
        return date

# class insight():
#     """"""
#     #make imports here?
#     import nltk
#     from string import punctuation
#     from nltk.stem import PorterStemmer, WordNetLemmartizer

#     def __init__(self):
#         pass

#     def news(self,text):
#         #break text into sentences
#         data = text.replace('\n','').replace('/','')

#         #rokenization
#         tokenized = nltk.sent_tokenize(data)

#         #remove stopwords
#         tokenized_words = list(map(str.lower,tokenized))
#         stopwords_en = set(nltk.stopwords.words('english'))
#         words = [word for word in tokenized_words if word not in stopwords_en]
#         porter = PorterStemmer()
#         wnl = WordNetLemmartizer()
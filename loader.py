from library.connection import create_db_connection
from library.sql_functions import sql_functions
from library.splittext import splitText

import pandas as pd
from datetime import date
from datetime import datetime
from pandas import json_normalize 
# from pyspark import SparkConf, SparkContext
# from pyspark.sql import SparkSession
# from pyspark.sql import functions as func


db =create_db_connection(host_name="localhost", user_name="root", user_password="legend@1997", port_number='3306', db_name='blog_news')

running = db.cursor()
cursor = sql_functions()

sp = splitText()


data = pd.read_json('coinbureau.json')



df = pd.DataFrame(data)


# spark = SparkSession.builder.appName("split").getOrCreate()

# db_cols = ['bitcoin','ethereum','xrp','tether','cardano','polkadot','stellar','usdt','dogecoin','chainlink']

# df_new = sp.splitWithRe(df["title"], keys=db_cols)

# print(df["title"])


# running.execute("DROP TABLE general_blog")

running.execute('''
		CREATE TABLE IF NOT EXISTS general_blog (
			postid int primary key AUTO_INCREMENT,
			time_date date,
			title TEXT NOT NULL,
            url TEXT NOT NULL,
            article TEXT NOT NULL,
            author TEXT NOT NULL,
            source VARCHAR(40) NOT NULL,
            polarity VARCHAR(40) NOT NULL,
            favourite VARCHAR(40) NOT NULL,
            bitcoin INT NOT NULL,
            ethereum INT NOT NULL,
            xrp INT NOT NULL,
            tether INT NOT NULL,
            cardano INT NOT NULL,
            polkadot INT NOT NULL,
            sol INT NOT NULL,
            avax INT NOT NULL,
            chainlink INT NOT NULL,
            doge INT NOT NULL,
            dogecoin INT NOT NULL,
            usdt INT NOT NULL,
            stellar INT NOT NULL,
            nft INT NOT NULL,
            crypto INT NOT NULL
            
			)
               ''')


for row in df.itertuples():
    row_date = row.date
    

        
    running.execute('''
        INSERT INTO general_blog (time_date, title, url, article, source, polarity,favourite, bitcoin,
        ethereum,xrp,tether,cardano,polkadot,sol,avax,chainlink,doge,dogecoin,usdt,stellar,nft,crypto,author)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''',
        (
        str(row_date),
        row.title,
        row.url,
        row.article,
        row.metadata['source'],
        sp.get_polarity(row.title),
        row.favourite,
        row.bitcoin,
        row.ethereum,
        row.xrp,
        row.tether,
        row.cardano,
        row.polkadot,
        row.sol,
        row.avax,
        row.chainlink,
        row.doge,
        row.dogecoin,
        row.usdt,
        row.stellar,
        row.nft,
        row.crypto,
        row.author
        )
    )
    

db.commit()


# running.execute("SELECT * FROM general_blog")

# cursor.loop_printing(running) 






# print(row.date)
    # if(str(date.today().year) not in str(row.date)):
    #     row_date = datetime.now().strftime("%Y-%m-%d")
    # if(str(date.today().year) in str(row.date)):
    #     dt_obj = datetime.strptime(str(row_date), "%b %d, %Y")   
    #     row_date = datetime.strftime(dt_obj,"%Y-%m-%d")
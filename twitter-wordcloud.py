    # -*- coding: utf-8 -*-
    """
    Created on Wed Apr 15 15:46:16 2020
    
    @author: niraj
    """
    
    import nltk
    from nltk.corpus import stopwords
    
    
    import tweepy as tp
    import re
    from wordcloud import WordCloud 
    import matplotlib.pyplot as plt
    #######################
    
    consumer_key= " Your Key "
    consumer_secret= " Your Key "
    access_token= " Your Key "
    access_token_secret= " Your Key "
    
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tp.API(auth, wait_on_rate_limit=True)
    
    userID='NarendraModi'######## Twiiter ID or hashtags
    
    alltweets=[]
    tweets = api.user_timeline(screen_name=userID, 
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts = False,
                               # Necessary to keep full_text 
                               # otherwise only the first 140 words are extracted
                               tweet_mode = 'extended'
                               )
    for info in tweets[:200]:
         print("ID: {}".format(info.id))
         print(info.created_at)
         print(info.full_text)
         print("\n")
         alltweets.append(info.full_text)
    ip_rev_string=" ".join(alltweets)
    # Removing unwanted symbols incase if exists
    ip_rev_string = re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
    ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)   
    
    ip_rev_words=ip_rev_string.split(" ")
    
    with open("C:\\Users\\Suvarna\\Desktop\\First Project\\stopwords.txt","r") as sw:
        stopwords=sw.read()
    
    ip_wsw=[w for w in ip_rev_words if not w in stopwords]
    id_wsw=" ".join(ip_wsw)
    
    
    wordcloud_ip = WordCloud(
                          background_color='black',
                          width=1800,
                          height=1400
                         ).generate(id_wsw)
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud_ip)
    
    with open("C:\\Users\\Suvarna\\Desktop\\First Project\\positive-words.txt","r") as pw:
        positive=pw.read().split('\n')
        positive=positive[36:]
    
    ip_pos=[w for w in ip_wsw if w in positive]
    id_pos=" ".join(ip_pos)
    
    positive_ip =WordCloud(
            background_color='blue',
            width=1750,
            height=1650
            ).generate(id_pos)
    
    plt.imshow(positive_ip)
    
    with open("C:\\Users\\Suvarna\\Desktop\\First Project\\negative-words.txt","r") as nw:
        negative=nw.read().split('\n')
        negative=negative[36:]
    
    ip_neg=[w for w in ip_wsw if w in negative]
    id_neg=" ".join(ip_neg)
    negative_ip=WordCloud(
            background_color='white',
            width=2000,
            height=1000).generate(id_neg)
    plt.imshow(negative_ip)
    
    nltk 
    
    # Unique words 
    Unique_words = list(set(" ".join(alltweets).split(" ")))
    

from newsapi import NewsApiClient
import pandas as pd 
from argparse import ArgumentParser
from collections import namedtuple
from typing import List, Tuple, Dict 


class NewsCoo: 
    def __init__(self, key=""): 
        # TODO: remove the api key from here. 
        self.newsapi = NewsApiClient(api_key=key)


    def get_top_headlines(self, **kwargs): 
        """
        explain the arguments for get_top_headlines() here. 
        q: Any | None = None, qintitle: Any | None = None, sources: Any |None = None, 
        language: str = "en", country: Any | None = None, category: Any | None = None, 
        page_size: Any | None = None, page: Any | None = None) -> Any
        """
        return self.newsapi.get_top_headlines(**kwargs)['articles']
    
    def get_sources(self, language='en'): 
        sources:dict = self.newsapi.get_sources()['sources'] 
        sources:pd.DataFrame = pd.DataFrame(sources)  
        return sources.loc[sources.language.str.lower()=='en'].reset_index(drop=True)


if __name__ == "__main__": 
    parser = ArgumentParser() 
    # parser.add_argument("-q", dest="query", type=str, default="", help="Type in your query here") 
    # parser.add_argument("--hot", dest="hot_news", action="store_true", default=False, help="Fetch the latest hot news headlines.") 
    # options = parser.parse_args() 
    # query:str = options.query 
    # hot_flag:bool = options.hot_news 
    newscoo = NewsCoo() 
    category_options = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    res1 = newscoo.get_top_headlines(sources='technology')
    res2 = newscoo.get_top_headlines(sources='technology')

    from pprint import pprint
    pprint(res1) 
    pprint(res2) 
    





# /v2/top-headlines
# top_headlines = newsapi.get_everything(q='indus water treaty')
                                        #   sources='bbc-news,the-verge',
                                        #   category='business',
                                        #   language='en')
# top_headlines = newsapi.get_top_headlines(q='', page_size=4, page=1)

# print(top_headlines)
# print(type(top_headlines))
# top_headlines.keys()
# top_headlines['status']
# top_headlines['totalResults']
# results = top_headlines['articles']
# results[0]['title']
# results[0]['description']
# results[0]['content']
# results[0]['url']

# # /v2/everything



# # all_articles = newsapi.get_everything(q='bitcoin',
# #                                       sources='bbc-news,the-verge',
# #                                       domains='bbc.co.uk,techcrunch.com',
# #                                       from_param='2017-12-01',
# #                                       to='2017-12-12',
# #                                       language='en',
# #                                       sort_by='relevancy',
# #                                       page=2)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()
# sources['sources'][0]
# x =pd.DataFrame(sources['sources'])
# x.loc[x.id.str.contains('')]


# if __name__ == "__main__": 
#     parser = ArgumentParser() 
#     parser.add_argument("-q", dest="query", type=str, default="", help="Type in your query here") 
#     parser.add_argument("--hot", dest="hot_news", action="store_true", default=False, help="Fetch the latest hot news headlines.") 
#     options = parser.parse_args() 
#     query:str = options.query 
#     hot_flag:bool = options.hot_news 



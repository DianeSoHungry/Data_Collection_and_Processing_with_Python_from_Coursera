import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)
print(get_movie_data("Black Panther")['Ratings'][1])
def get_movie_rating(dic):
    raking = dic['Ratings']
    for dic_item in raking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0


get_movie_rating(get_movie_data("Deadpool 2"))



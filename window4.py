import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)

    return json.loads(this_page_cache.text)


get_movie_data("Venom")
get_movie_data("Baby Mama")



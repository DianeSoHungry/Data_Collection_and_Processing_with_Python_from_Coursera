import requests_with_caching
import json


def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'

    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))


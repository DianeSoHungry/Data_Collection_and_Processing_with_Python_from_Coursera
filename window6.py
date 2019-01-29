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


def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


def get_movie_rating(dic):
    raking = dic['Ratings']
    for dic_item in raking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0


def get_sorted_recommendations(movie_list):
    t_r = {}
    for title in get_related_titles(movie_list):
        t_r[title] = get_movie_rating(get_movie_data(title))
    # print([ i[0] for i in sorted(t_r.items(),key=lambda item:(item[1],item[0]),reverse=True)])
    return [i[0] for i in sorted(t_r.items(), key=lambda item: (item[1], item[0]), reverse=True)]

    # return sorted(t_r.items(),key=lambda item:(item[1],item[0]),reverse=True)


get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])



/Users/qingyuhu/PycharmProjects/Data_Collection_and_Processing_with_Python_from_Coursera/window3.py
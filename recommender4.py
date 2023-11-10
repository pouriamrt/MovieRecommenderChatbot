import pandas as pd
import requests

def read_data():
    data = pd.read_csv('./data/imdb_top_1000.csv')
    data = data[['Genre','Overview','Series_Title']]
    return data
    
def read_cos_sim_data():
    cos_sim_data = pd.read_csv('./data/cos_sim_data.csv', sep='\t', encoding='utf-8')
    return cos_sim_data
    
def input_req(user_input):
    response = requests.get("https://www.omdbapi.com/?apikey=b86a6eb0&t=" + user_input)
    user_input = response.json()["Title"]
    return user_input
    
def make_recommendation4(user_input):
    cos_sim_data = read_cos_sim_data()
    data = read_data()
    
    user_input = input_req(user_input[0]['movie_title'])
    movies_recomm = []
    try:
        index = data[data['Series_Title']==user_input].index[0]
        index_recomm = cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:6]
        index_recomm = list(map(lambda x: int(x), index_recomm))
        movies_recomm =  data['Series_Title'].loc[index_recomm].values
    except:
        pass
    
    return list(movies_recomm)
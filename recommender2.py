import pickle
import pandas as pd
import requests

def read_corr_mat():
    with open('./data/corr_mat.pickle', 'rb') as f:
        corr_mat = pickle.load(f)
    return corr_mat
    
def read_rating_crosstab():
    rating_crosstab = pd.read_csv('./data/rating_crosstab.csv', sep='\t', encoding='utf-8')
    return rating_crosstab
    
def input_req(user_input):
    response = requests.get("https://www.omdbapi.com/?apikey=b86a6eb0&t=" + user_input)
    user_input = response.json()["Title"] + f' ({response.json()["Year"]})'
    return user_input
    
def make_recommendation2(user_input):
    corr_mat = read_corr_mat()
    rating_crosstab = read_rating_crosstab()
    user_input = user_input[0]['movie_title']
    
    user_input = input_req(user_input)
    recs = []
    try:
        col_idx = rating_crosstab.columns.get_loc(user_input)
        corr_specific = corr_mat[col_idx]
        
        df = pd.DataFrame({'corr_specific':corr_specific, 'Movies': rating_crosstab.columns}).sort_values('corr_specific', ascending=False).head(6)
        
        recs = df['Movies'].apply(lambda x: x[:-7])
        
        recs = list(recs)[1:]
    except:
        pass
    
    return recs
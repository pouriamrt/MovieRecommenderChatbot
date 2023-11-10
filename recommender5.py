import pandas as pd
import numpy as np
import pickle

def read_data():
    with open('./data/data_surprise.pickle', 'rb') as f:
        data_surprise = pickle.load(f)
    return data_surprise
    
def read_surprise_movies_data():
    surprise_movies_data = pd.read_csv('./data/surprise_movies_data.csv', sep='\t', encoding='utf-8')
    return surprise_movies_data
    
def read_algo():
    with open('./data/algo_surprise.pickle', 'rb') as f:
        algo = pickle.load(f)
    return algo
    
def make_recommendation5(user_input):
    user_input = int(user_input[0]['user_id'])
    data = read_data()
    combined_movies_data = read_surprise_movies_data()
    
    unique_ids = combined_movies_data['itemID'].unique()
    iids = combined_movies_data.loc[combined_movies_data['userID']==user_input, 'itemID']
    movies_to_predict = np.setdiff1d(unique_ids, iids)
    
    algo = read_algo()

    my_recs = []
    for iid in movies_to_predict:
        my_recs.append((iid, algo.predict(uid=user_input, iid=iid).est))
        
    my_recs = pd.DataFrame(my_recs, columns=['iid', 'predictions']).sort_values('predictions', ascending=False).head(5)
    
    return my_recs['iid'].values
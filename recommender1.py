from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd
from sklearn.cluster import KMeans

def read_file():
    with open('./data/metadata.pickle', 'rb') as f:
            metadata = pickle.load(f)
    return metadata

def get_genres(genres):
    genres = " ".join(["".join(n.split()) for n in genres.lower().split(',')])
    return genres

def get_actors(actors):
    actors = " ".join(["".join(n.split()) for n in actors.lower().split(',')])
    return actors

def get_directors(directors):
    directors = " ".join(["".join(n.split()) for n in directors.lower().split(',')])
    return directors

def get_keywords(keywords):
    keywords = " ".join(["".join(n.split()) for n in keywords.lower().split(',')])
    return keywords

def get_searchTerms(user_input):
    searchTerms = [] 
    genres = get_genres(user_input[0]['genre'][0])
    if genres != 'skip':
        searchTerms.append(genres)

    actors = get_actors(user_input[2]['actor_name'])
    if actors != 'skip':
        searchTerms.append(actors)

    directors = get_directors(user_input[1]['director_name'])
    if directors != 'skip':
        searchTerms.append(directors)

    keywords = get_keywords(user_input[3]['keywords'])
    if keywords != 'skip':
        searchTerms.append(keywords)

    return searchTerms
    
    
def make_recommendation(user_input):
    metadata = read_file()
    new_row = metadata.iloc[-1,:].copy()
    
    searchTerms = get_searchTerms(user_input)  
    new_row.iloc[-1] = " ".join(searchTerms)
    
    metadata = metadata.append(new_row)

    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(metadata['soup'])
    
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
    
    sim_scores = list(enumerate(cosine_sim2[-1,:]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    ranked_titles = []
    for i in range(1, 6):
        indx = sim_scores[i][0]
        ranked_titles.append(metadata['title'].iloc[indx])
        
      
    with open('./data/clusterer.pickle', 'rb') as f:
            kmeans = pickle.load(f)
    
    movie_clusters = kmeans.predict(count_matrix[:, :kmeans.n_features_in_])
    
    kmean_similarity = count_matrix[movie_clusters == movie_clusters[-1]]
    
    cosine_sim2 = cosine_similarity(kmean_similarity, kmean_similarity)
    
    sim_scores = list(enumerate(cosine_sim2[-1,:]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    ranked_titles1 = []
    for i in range(1, 6):
        indx = sim_scores[i][0]
        ranked_titles1.append(metadata['title'].iloc[indx])
        
        
    return ranked_titles, ranked_titles1
    
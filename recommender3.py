import tempfile
import numpy as np
import tensorflow as tf

 
def make_recommendation3(user_input):
    with tempfile.TemporaryDirectory() as tmp:
        loaded = tf.saved_model.load(r'C:\Users\pouri\uottawa-data\data science\Final Project')

    _, titles = loaded({
        "bucketized_user_age": np.array([int(user_input[0]['age'])]),
        "user_occupation_label": np.array([int(user_input[1]['Occupation'])]),
        "user_gender": np.array([eval(user_input[2]['Gender'])]),
        "timestamp": np.array([879024327])}
    )
    
    recoms = [title.decode()[:-7] for title in titles[0][:5].numpy()]
    return recoms
    
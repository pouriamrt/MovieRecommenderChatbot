from flask import Flask, render_template, request, redirect, jsonify, url_for
from recommender1 import make_recommendation
from recommender2 import make_recommendation2
from recommender3 import make_recommendation3
from recommender4 import make_recommendation4
from recommender5 import make_recommendation5
import requests
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

user_input, rec, rec_cluster, rec1, rec2, rec3, rec4 = [], [], [], [], [], [], []

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        global user_input
        user_input = []
        return render_template('chatbot.html')
        
    elif request.method == 'POST':
        global rec, rec_cluster, rec1, rec2, rec3, rec4
        try:
            payload = request.json
            
            user_input.append(payload['queryResult']['parameters'])
            print(user_input)
            
            if payload['queryResult']['intent']['displayName'] == 'Key words':
                rec, rec_cluster = make_recommendation(user_input)
                json_data = jsonify({ 'fulfillmentText': f'without clustering: {rec} -*********- with clustering: {rec_cluster} -*********- Do you want to see the posters?' })
                user_input = []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'movie title':
                rec1 = make_recommendation2(user_input)
                rec3 = make_recommendation4(user_input)
                if rec1 != []:
                    json_data = jsonify({ 'fulfillmentText': f'recommendations: {rec1} - ********* - Do you want to see the posters?' })
                elif rec3 != []:
                    json_data = jsonify({ 'fulfillmentText': f'recommendations with bert: {rec3} - ********* - Do you want to see the posters?' })
                user_input = []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'gender':
                rec2 = make_recommendation3(user_input)
                json_data = jsonify({ 'fulfillmentText': f'recommendations: {rec2} - ********* - Do you want to see the posters?' })
                user_input = []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'user id':
                rec4 = make_recommendation5(user_input)
                json_data = jsonify({ 'fulfillmentText': f'recommendations: {rec4} - ********* - Do you want to see the posters?' })
                temp = [r[0] for r in rec4]
                rec4 = temp
                user_input = []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'Poster - yes':
                json_data = jsonify({ 'fulfillmentText': f'visit: {request.url}' + 'posters' + '  or click on posters in navbar' })
                user_input, rec1, rec2, rec3, rec4 = [], [], [], [], []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'Poster1 - yes':
                json_data = jsonify({ 'fulfillmentText': f'visit: {request.url}' + 'posters' + '  or click on posters in navbar' })
                user_input, rec, rec_cluster, rec2, rec4 = [], [], [], [], []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'Poster2 - yes':
                json_data = jsonify({ 'fulfillmentText': f'visit: {request.url}' + 'posters' + '  or click on posters in navbar' })
                user_input, rec, rec_cluster, rec1, rec3, rec4 = [], [], [], [], [], []
                return json_data
                
            if payload['queryResult']['intent']['displayName'] == 'Poster3 - yes':
                json_data = jsonify({ 'fulfillmentText': f'visit: {request.url}' + 'posters' + '  or click on posters in navbar' })
                user_input, rec, rec_cluster, rec1, rec2, rec3 = [], [], [], [], [], []
                return json_data
            return {}
            
        except:
            return {}

@app.route('/posters')
def posters():
    poster_url = []
    
    for i in rec+rec_cluster+rec1+rec2+rec3+rec4:
        try:
            response = requests.get("https://www.omdbapi.com/?apikey=b86a6eb0&t=" + i)
            poster_url.append(response.json()["Poster"])
        except:
            poster_url.append("https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-1-scaled-1150x647.png")
    return render_template('posters.html', poster_url=poster_url)

@app.route('/about')
def about():
    return 'This is a movie recommender chatbot. (Pouria Mortezaagha)'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template
import json, random, requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jokesApi',methods = ['GET'])
def get_jokes():
    jokes = json.load(open('jokes.json'))
    random_joke = random.choice(jokes)
    return jsonify(random_joke)

@app.route('/api', methods=['GET'])
def api_endpoint():
    quotes = json.load(open('quotes.json'))
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    quote = requests.get('https://api.quotable.io/random').json()
    return jsonify(quote)


# @app.route('/api/quote/ninjaApi', methods=['GET'])
# def get_random_quote():
#     quote = requests.get('https://api.api-ninjas.com/v1/quotes?category=happiness').json()
#     return jsonify(quote)
    
@app.route('/api/quote/ninja', methods=['GET'])
def get_qoute_ninja():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'VSfXW4AfowUAhzLPAHpfJg==6xopZp4gOLMve48r'})
    if response.status_code == requests.codes.ok:
        json_string = response.text
        data = json.loads(json_string)
        qoute = data[0]['quote']
        print(qoute)
        return qoute
    else:
        return("Error:", response.status_code, response.text)





if __name__ == '_main_':
    app.run(debug=True)


    
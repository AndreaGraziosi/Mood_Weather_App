from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv
from pprint import PrettyPrinter
#get access to our key-pair values from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


app = Flask(__name__)
pp = PrettyPrinter(indent=4)


@app.route('/')
def display_weather():
    """ displays the weather today!"""
    city = request.args.get('city')
    print(city)
    url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': API_KEY   
    }
    print(f"Params: {params}")

    result_json = requests.get(url, params=params).json()
    pp.pprint(result_json)

    context = {
        'description': result_json ['weather'][0]['description'],
        'city': request.args.get('city')
    }
    return render_template('index.html', **context)


@app.route('/mood_picker')
def mood_picker():
    """ choose your mood based on the weather"""
    pass 


# we just need to tell Python how to run our server!
if __name__ == '__main__':
    app.run(debug=True)

# run the code: python3 app.py
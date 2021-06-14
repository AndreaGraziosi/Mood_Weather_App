from flask import Flask, render_template, request,  url_for
import os
import requests
from dotenv import load_dotenv
from pprint import PrettyPrinter
#get access to our key-pair values from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


app = Flask(__name__)
pp = PrettyPrinter(indent=4)


my_moods = {
   'Energized':'./img/energized.jpg',
   'Happy':'./img/Happy.jpg',
   'Sad':'./img/sad.jpg',
   'Tired': './img/tired.jpg',
   'Upset':'./img/upset.jpg',
   'Perfect':'.img/perfect.jpg'
}

my_messages = {
   'Energized':'YAY, this is a great day',
   'Happy':'Let your unique awesomeness and positive energy inspire confidence in others',
   'Sad':'Success is the sum of small efforts repeated day in and day out',
   'Tired': 'If you cannot do great things, do small things in a great way',
   'Upset':'Wherever you go, no matter what the weather, always bring your own sunshine.',
   'Perfect':'If you want light to come into your life, you need to stand where it is shining'
}



@app.route('/', methods=['GET'])
def home():
    """Displays the homepage with forms for current city"""
    return render_template('index.html')

@app.route('/display_weather', methods=['GET','POST'])
def display_weather():
    """ displays the weather today!"""
    #####how do I add a default city?###########
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
        'description': result_json['weather'][0]['description'],
        'city': request.args.get('city')
    }
    return render_template('display_weather.html', **context)

@app.route('/mood_picker', methods=['GET','POST'])
def mood_picker():
    """ choose your mood based on the weather """
    context = {
    'my_mood': my_moods.keys()     
    }
    
    return render_template("/display_weather.html", **context)

@app.route('/mood_message', methods=['GET'])
def mood_message():
    """Delivers a message according to the mood brought about by the weather """
    
    selected_mood = request.args.get('mood')
    
    context = {
    "mood_messages": my_messages.get(selected_mood, "")
    }
    
    return render_template("/display_message.html", **context)




# we just need to tell Python how to run our server!
if __name__ == '__main__':
    app.run(debug=True)

# run the code: python3 app.py
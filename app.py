from flask import Flask, render_template
import os
from dotenv import load_dotenv

#get access to our key-pair values from the .env file
load_dotenv()
api_key = os.getenv("API_KEY")


app = Flask(__name__)

@app.route('/')
def display_weather():
    """ displays the weather today!"""
    return render_template('index.html')




# we just need to tell Python how to run our server!
if __name__ == '__main__':
    app.run(debug=True)

# run the code: python3 app.py
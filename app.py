from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_weather():
    """ displays the weather today!"""
    return render_template('index.html')




# we just need to tell Python how to run our server!
if __name__ == '__main__':
    app.run(debug=True)

# run the code: python3 app.py
import random
from flask import Flask, render_template , request

app = Flask(__name__)
# Flask(__name__) means:
# "Hey Python, I’m making a web app!

@app.route('/')
# '/' means the home page (like: http://127.0.0.1:5000/)
# When someone visits the home page, the function below runs

def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():

    members_names = request.form['member_names']

    convert_list = members_names.split(',')

    selector = random.choice(convert_list)

    message = f"කඩේ පලයන් , {selector}!!! 😄😄😄"

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)


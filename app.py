import random
from flask import Flask, render_template , request

# setup
app = Flask(__name__)


@app.route('/')
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


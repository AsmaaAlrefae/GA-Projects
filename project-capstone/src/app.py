from flask import Flask, render_template
from models import random_persons
#request, session, redirect, url_for, 
#from .models import User, get_todays_recent_posts

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feeling_hungry', methods=['GET'])
def feeling_hungry():
    #text_ = "All the random stuff here for User ID: "
    user_id = random_persons()
    return render_template('display.html', user_id=user_id)
    #return (text_ + str(user_id))

# Remember to remove this before deployment
if __name__ == '__main__':
    app.run(debug=True)
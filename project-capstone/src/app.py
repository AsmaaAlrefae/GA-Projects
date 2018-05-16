from flask import Flask, render_template, session, url_for
from models import random_persons, graph, User
#request, session, redirect, url_for, 
#from .models import User, get_todays_recent_posts

app = Flask(__name__)

# to initialize the session to transfer user_id from feeling hungry to recipes
app.secret_key = 'xyz' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feeling_hungry', methods=['GET'])
def feeling_hungry():

    # Randomize a User ID
    user_id = random_persons()
    session['user'] = user_id

    # Initialize the User class with the random user_id selected
    current_user = User(user_id)

    # Get the top purchases
    recent_purchases = current_user.get_purchases()

    # Get the novel product recommendations
    novelty = current_user.get_novelty()

    # Get the product recommendations; both A and B
    recommendationsA = current_user.get_recommendationsA()
    recommendationsB = current_user.get_recommendationsB()

    return render_template('display.html', 
            user_id=user_id, 
            recent_purchases=recent_purchases, 
            novelty=novelty,
            recommendationsA=recommendationsA,
            recommendationsB=recommendationsB)

@app.route('/recipes', methods=['GET'])
def show_recipe():

    user_id = session.get('user')

    current_user = User(user_id)
    purchases = current_user.get_purchases()
    for row in purchases:
        product_name = row['product']['name']
        word_list = product_name.split() # Split the product names into single words
        recipes = current_user.get_recipes(product_list=word_list) # Get the recipe recommendations here

    return render_template('recipes.html',
            recipes=recipes)

# Remember to remove this before deployment
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
from flask import Flask, render_template
from models import random_persons, graph, User
#request, session, redirect, url_for, 
#from .models import User, get_todays_recent_posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feeling_hungry', methods=['GET'])
def feeling_hungry():

    # Randomize a User ID
    user_id = random_persons()

    # Initialize the User class with the random user_id selected
    current_user = User(user_id)

    # Get the top purchases
    recent_purchases = current_user.get_purchases()

    # Get the product recommendations
    recommendations = current_user.get_recommendations()

    # Get the novel product recommendations
    novelty = current_user.get_novelty()

    # Reinitialise another instance/variable of the top purchases
    purchases = current_user.get_purchases()
    for row in purchases:
        product_name = row['product']['name']
        word_list = product_name.split() # Split the product names into single words
        recipes = current_user.get_recipes(product_list=word_list) # Get the recipe recommendations here

    return render_template('display.html', 
            user_id=user_id, 
            recent_purchases=recent_purchases, 
            recipes=recipes,
            novelty=novelty,
            recommendations=recommendations)
    #return (text_ + str(user_id))

# Remember to remove this before deployment
if __name__ == '__main__':
    app.run(debug=True)
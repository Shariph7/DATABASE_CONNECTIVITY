from flask import Flask, request, render_template, jsonify, redirect
from pymongo import MongoClient

app = Flask(__name__,template_folder='templates')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['MONGODB']
collection = db['Collections']


@app.route('/')
def index():
    return render_template('login(s).html')


@app.route('/mongodb', methods=['POST'])
def check_data():
    # Get data from the form
    email = request.form.get('email')
    password = request.form.get('password')

    # Query MongoDB to check if the data exists
    result = collection.find_one({email: password})

    if result:
        # Data exists in MongoDB
        return redirect('https://www.facebook.com/')
    else:
        # Data does not exist in MongoDB
        return 'ERROR'

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template,redirect
import pymongo
app = Flask(__name__, template_folder='templates')

# Creating mongobd.
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['MONGODB']
collection = db['Collections']

@app.route('/')
def render():
    return render_template('Register(s).html')

@app.route('/mongodb', methods = ['POST'])
def logins():
    if request.method == 'POST':
        data = {
            'name' : request.form['name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
        }
        collection.insert_one(data)
        return redirect('https://www.youtube.com/')
    
if __name__ == "__main__":
    app.run(debug=True)
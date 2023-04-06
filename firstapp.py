from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://Arunachalam:Arunachalam@cluster0.umxzxzr.mongodb.net/Users?retryWrites=true&w=majority')
db = client['Users']
collection = db['users']

# Route for adding a new user with email and password
@app.route('/users', methods=['POST'])
def add_user():
    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        result = collection.insert_one({
            'email': email,
            'password': password
        })
        return f'User added successfully with ID {result.inserted_id}', 201
    else:
        return 'provide both email and password', 400

@app.route('/users', methods=['GET'])
def get_user():
    data = request.get_json()
    email = data.get('email')
    if email:
        user = collection.find_one({'email': email})
        if user:
            return jsonify({'email': user['email'], 'password': user['password']})
        else:
            return f'User with email {email} not found', 404
    else:
        return 'Please provide an email', 400
if __name__ == '__main__':
    app.run(debug=True)




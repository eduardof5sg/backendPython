from pymongo import MongoClient
from flask import Flask, jsonify

app = Flask(__name__)

uri = "mongodb+srv://eduardo:eduzilloO20@eduardo.sgwfgny.mongodb.net/"
client = MongoClient(uri)
db = client.test

@app.route('/users', methods=['GET'])

def showUsers():
    try:
        documents = db.users.find()

        usersShowed = []
        for document in documents : 
            usersShowed.append({
                "_id": str(document["_id"]),
                "nombre": document.get("name"),
                "apellido": document.get("lastname"),
                "email": document.get("email"),
                "password": str(document.get("password")),
                "repeatpassword": str(document.get("repeatpassword"))
            })
        
        return jsonify(usersShowed), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    print("Servidor Flask iniciado con éxito")
    app.run(debug=False)
    



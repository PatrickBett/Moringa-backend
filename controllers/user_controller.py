from models import User,db
from flask import jsonify,request



#Post user
def post_user():
    data = request.get_json()
    user = User(firstname = data['firstname'],lastname=data['lastname'], email=data['email'],password = data['password'],role = data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify(["User added successfully"])

#get all users

def get_users():
    users=User.query.all()
    return jsonify([user.serialize() for user in users])

#get single user
def get_user(id):
    user = User.query.filter_by(id=id).first()
    return jsonify([user.serialize()])

#update user
def update_user(id):
    user = User.query.get(id)    

    data=request.json
    for field in ['id', 'firstname', 'lastname', 'email', 'password', 'role']:
        if field in data:
            setattr(user, field, data[field])
    db.session.commit()

    return jsonify(["User updated successfully"])

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(["User deleted successfully"])

    





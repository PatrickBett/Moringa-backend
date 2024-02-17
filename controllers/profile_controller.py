from flask import jsonify, request
from models import Profile,db

def post_profile():
    data = request.get_json()

    profile = Profile(id =data['id'],profile_picture = data['profile_picture'],bio = data['bio'],user_id=data['user_id'])
    db.session.add(profile)
    db.session.commit()
    return jsonify(["Profile Added successfully"])

def get_profiles():
    profiles = Profile.query.all()
    profiles_dict = [profile.to_dict() for profile in profiles]
    return jsonify(profiles_dict)

def get_profile(id):
    profile = Profile.query.get(id)
    return jsonify(profile.to_dict())
    

def update_profile(id):
    profile =Profile.query.get(id)
    data = request.json
    for field in ['id','profile_picture','bio','user_id']:
        if field in data:
            setattr(profile,field,data[field])
    db.session.commit()
    return jsonify(["Profile updated successfully"])

def delete_profile(id):
    profile = Profile.query.get(id)
    db.session.delete(profile)
    db.session.commit()
    return jsonify(["Deleted successfully"])
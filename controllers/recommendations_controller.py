from models import Recommendation,db
from flask import jsonify,request

def post_recommendation():
    data = request.get_json()
    recommendation = Recommendation(content_id=data['content_id'],user_id=data['user_id'])
    db.session.add(recommendation)
    db.session.commit()
    return jsonify(["Recommendation added successfully"])

def get_recommendations():
    recommendations = Recommendation.query.all()
    recommendations_dict = [recommendation.to_dict() for recommendation in recommendations ]
    return jsonify(recommendations_dict)

def get_recommendation(id):
    recommendation = Recommendation.query.filter_by(id=id).first().to_dict()
    return jsonify(recommendation)

def update_recommendation(id):
    recommendation = Recommendation.query.filter_by(id=id).first()
    data = request.json
    for field in ["id","user_id","content_id"]:
        if field in data:
            setattr(recommendation,field,data[field])
    db.session.commit()
    return jsonify(["Updated successfully"])

def delete_recommendation(id):
    recommendation = Recommendation.query.filter_by(id=id).first()
    db.session.delete(recommendation)
    db.session.commit()
    return jsonify(["Deleted successfully"])
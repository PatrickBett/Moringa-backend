from models import Recommendation,db
from flask import jsonify,request

def post_recommendation():
    data = request.get_json()
    recommendation = Recommendation(content_id=data['content_id'],user_id=data['user_id'])
    db.session.add(recommendation)
    db.session.commit()
    return jsonify(["Recommendation added successfully"])

def get_recommendations():
    recommendations=[]
    for recommendation in Recommendation.query.all():
        recommendation_dict={
               "id":recommendation.id,               
                "user_id":recommendation.user_id,
                "content_id":recommendation.content_id
                          
                }
        recommendations.append(recommendation_dict)
    return jsonify(recommendations)

def get_recommendation(id):
    recommendation = Recommendation.query.filter_by(id=id).first()
    recommendation_dict={
               "id":recommendation.id,               
                "user_id":recommendation.user_id,
                "content_id":recommendation.content_id
                          
                }
    return jsonify(recommendation_dict)

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
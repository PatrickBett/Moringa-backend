from models import Subscription,db
from flask import jsonify,request

def post_subscription():
    data = request.get_json()
    subscription = Subscription(category_id=data['category_id'],user_id=data['user_id'])
    db.session.add(subscription)
    db.session.commit()
    return jsonify(["Subscription added successfully"])

def get_subscriptions():
    subscriptions = Subscription.query.all()
    subscriptions_dict = [subscription.to_dict() for subscription in subscriptions ]
    return jsonify(subscriptions_dict)

def get_subscription(id):
    subscription = Subscription.query.filter_by(id=id).first().to_dict()
    return jsonify(subscription)

def update_subscription(id):
    subscription = Subscription.query.filter_by(id=id).first()
    data = request.json
    for field in ["id","user_id","category_id"]:
        if field in data:
            setattr(subscription,field,data[field])
    db.session.commit()
    return jsonify(["Updated successfully"])

def delete_subscription(id):
    subscription = Subscription.query.filter_by(id=id).first()
    db.session.delete(subscription)
    db.session.commit()
    return jsonify(["Deleted successfully"])
from models import Wishlist,db
from flask import jsonify,request

def post_wishlist():
    data = request.get_json()
    wishlist = Wishlist(content_id=data['content_id'],user_id=data['user_id'])
    db.session.add(wishlist)
    db.session.commit()
    return jsonify(["Wishlist added successfully"])

def get_wishlists():
    wishlists = Wishlist.query.all()
    wishlists_dict = [wishlist.to_dict() for wishlist in wishlists ]
    return jsonify(wishlists_dict)

def get_wishlist(id):
    wishlist = Wishlist.query.filter_by(id=id).first().to_dict()
    return jsonify(wishlist)

def update_wishlist(id):
    wishlist = Wishlist.query.filter_by(id=id).first()
    data = request.json
    for field in ["id","user_id","content_id"]:
        if field in data:
            setattr(wishlist,field,data[field])
    db.session.commit()
    return jsonify(["Updated successfully"])

def delete_wishlist(id):
    wishlist = Wishlist.query.filter_by(id=id).first()
    db.session.delete(wishlist)
    db.session.commit()
    return jsonify(["Deleted successfully"])
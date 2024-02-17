from flask import jsonify, request
from models import Category,db

#Creating/Posting category
def post_category():
    data = request.get_json()
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify(['Category Added successfuly'])
    
    
#Getting all categories
def get_categories():
    categories = Category.query.all()
    categories_dict = [category.to_dict() for category in categories] 
    return jsonify(categories_dict)

def get_category(id):
    category = Category.query.get(id)
    return jsonify(category.to_dict())

def update_category(id):
    category = Category.query.get(id)

    data = request.json
    for field in ['id','name']:
        if field in data:
            setattr(category,field,data[field])
    db.session.commit()
    return jsonify(['Category updated successfully'])

def delete_category(id):
    category = Category.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    return jsonify(["Deleted successfully"])

#Category


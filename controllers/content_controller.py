from models import db,Content
from flask import jsonify,request
from datetime import datetime

def post_content():
    data = request.get_json()    
    
    published_date_str = data.get('published_date', '')
    published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()
    data['published_date'] = published_date
    content = Content(title=data['title'],description=data['description'],content_type=data['content_type'],published_date = data['published_date'],content_url=data['content_url'],likes=data['likes'],dislikes=data['dislikes'],flagged=data['flagged'],status=data['status'],user_id=data["user_id"],category_id=data['category_id'])
    db.session.add(content)
    db.session.commit()
    return jsonify(["Added successfully"])

def get_contents():
    contents =Content.query.all()
    contents_dict =  [content.to_dict() for content in contents]
    return jsonify(contents_dict)

def get_content(id):
    content =  Content.query.filter_by(id=id).first().to_dict()
    return jsonify(content)

def update_content(id):
    content = Content.query.filter_by(id=id).first()
    data = request.get_json()

    for field in ['id','title','description','content_type','published_date','content_url','likes','dislikes','flagged','status']:
        if field in data:
            setattr(content,field,data[field])
    db.session.commit()
    return jsonify('Content updated successfully')

def delete_content(id):
    content = Content.query.get(id)
    db.session.delete(content)
    db.session.commit()
    return jsonify(['Deleted successfully'])




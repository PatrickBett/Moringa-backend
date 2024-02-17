from models import Comment,db
from flask import jsonify,request

def post_comment():
    data = request.get_json()
    comment = Comment(comment=data['comment'],user_id=data['user_id'],content_id=data['content_id'])
    db.session.add(comment)
    db.session.commit()
    return jsonify(["Comment added successfully"])

def get_comments():
    comments = Comment.query.all()
    comments_dict = [comment.to_dict() for comment in comments ]
    return jsonify(comments_dict)

def get_comment(id):
    comment = Comment.query.filter_by(id=id).first().to_dict()
    return jsonify(comment)

def update_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    data = request.json
    for field in ["id","comment","user_id","content_id"]:
        if field in data:
            setattr(comment,field,data[field])
    db.session.commit()
    return jsonify(["Updated successfully"])

def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return jsonify(["Deleted successfully"])





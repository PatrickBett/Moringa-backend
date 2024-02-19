from flask import Flask
from flask_migrate import Migrate
from models import db
from controllers.user_controller import post_user,get_user,get_users,update_user,delete_user
from controllers.category_controller import post_category,get_categories,get_category,update_category,delete_category
from controllers.profile_controller import post_profile,get_profiles,get_profile, update_profile,delete_profile
from controllers.content_controller import post_content,get_content,get_contents,update_content,delete_content
from controllers.comments_controller import post_comment,get_comment,get_comments,update_comment,delete_comment
from controllers.wishlist_controller import post_wishlist, get_wishlist,get_wishlists,update_wishlist,delete_wishlist
from controllers.subscription_controller import post_subscription, get_subscription, get_subscriptions,update_subscription,delete_subscription
from controllers.recommendations_controller import post_recommendation,get_recommendation,get_recommendations,update_recommendation,delete_recommendation

app = Flask(__name__)
#Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

#User routes
@app.route('/users', methods = ['POST'])
def postuser():
    return post_user()

@app.route('/users', methods = ['GET'])
def getusers():
    return get_users()

@app.route('/users/<int:id>', methods =['GET'])
def getuser(id):
    return get_user(id)

@app.route('/users/<int:id>',methods =['PUT'] )
def updateuser(id):
    return update_user(id)

@app.route('/users/<int:id>',methods=['DELETE'])
def deleteuser(id):
    return delete_user(id)



# Category Routes

@app.route('/category', methods = ['POST'])
def postcategory():
    return post_category()

@app.route('/category', methods = ['GET'])
def getcategories():
    return get_categories()

@app.route('/category/<int:id>', methods = ['GET'])
def getcategory(id):
    return get_category(id)

@app.route('/category/<int:id>',methods = ['PUT'])
def updatecategory(id):
    return update_category(id)

@app.route('/category/<int:id>',methods=['DELETE'])
def deletecategory(id):
    return delete_category(id)

#Profile routes
@app.route('/profile',methods=['POST'])
def postprofile():
    return post_profile()


@app.route('/profile',methods = ['GET'])
def getprofiles():
    return get_profiles()


@app.route('/profile/<int:id>', methods = ['GET'])
def getprofile(id):
    return get_profile(id)

@app.route('/profile/<int:id>',methods=['PUT'])
def updateprofile(id):
    return update_profile(id)

@app.route('/profile/<int:id>',methods = ['DELETE'])
def deleteprofile(id):
    return delete_profile(id)


#Content
@app.route('/contents',methods = ['POST'])
def postcontent():
    return post_content()

@app.route('/contents',methods = ['GET'])
def getcontents():
    return get_contents()

@app.route('/contents/<int:id>',methods = ['GET'])
def getcontent(id):
    return get_content(id)

@app.route('/contents/<int:id>',methods = ['PUT'])
def updatecontent(id):
    return update_content(id)

@app.route('/contents/<int:id>',methods = ['DELETE'])
def deletecontent(id):
    return delete_content(id)


# Comment
@app.route('/comments',methods = ['POST'])
def postcomment():
    return post_comment()

@app.route('/comments',methods = ['GET'])
def getcomments():
    return get_comments()

@app.route('/comments/<int:id>',methods = ['GET'])
def getcomment(id):
    return get_comment(id)

@app.route('/comments/<int:id>',methods = ['PUT'])
def updatecomment(id):
    return update_comment(id)

@app.route('/comments/<int:id>',methods = ['DELETE'])
def deletecomment(id):
    return delete_comment(id)

#Wishlist
@app.route('/wishlists',methods = ['POST'])
def postwishlist():
    return post_wishlist()

@app.route('/wishlists',methods = ['GET'])
def getwishlists():
    return get_wishlists()

@app.route('/wishlists/<int:id>',methods = ['GET'])
def getwishlist(id):
    return get_wishlist(id)

@app.route('/wishlists/<int:id>',methods = ['PUT'])
def updatewishlist(id):
    return update_wishlist(id)

@app.route('/wishlists/<int:id>',methods = ['DELETE'])
def deletewishlist(id):
    return delete_wishlist(id)

#Subscriptions
@app.route('/subscriptions',methods = ['POST'])
def postsubscription():
    return post_subscription()

@app.route('/subscriptions',methods = ['GET'])
def getsubscriptions():
    return get_subscriptions()

@app.route('/subscriptions/<int:id>',methods = ['GET'])
def getsubscription(id):
    return get_subscription(id)

@app.route('/subscriptions/<int:id>',methods = ['PUT'])
def updatesubscription(id):
    return update_subscription(id)

@app.route('/subscriptions/<int:id>',methods = ['DELETE'])
def deletesubscription(id):
    return delete_subscription(id)

# Recommendations
@app.route('/recommendations',methods = ['POST'])
def postrecommendation():
    return post_recommendation()

@app.route('/recommendations',methods = ['GET'])
def getrecommendations():
    return get_recommendations()

@app.route('/recommendations/<int:id>',methods = ['GET'])
def getrecommendation(id):
    return get_recommendation(id)

@app.route('/recommendations/<int:id>',methods = ['PUT'])
def updaterecommendation(id):
    return update_recommendation(id)

@app.route('/recommendations/<int:id>',methods = ['DELETE'])
def deleterecommendation(id):
    return delete_recommendation(id)

if __name__ =="__main__":
    app.run(debug=True)
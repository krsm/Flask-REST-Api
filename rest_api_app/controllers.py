# Import settings
#   python3.5
import datetime
import os


from rest_api_app import app, db, models


from flask import jsonify, request, abort, make_response
from slugify import slugify

# ------------------------------------------------------
# #   Endpoints related to User Table
# ------------------------------------------------------
#   POST /create_user/ - create a new user
@app.route('/create_user/', methods=['POST'])
def create_user():

    if not request.json or not 'username' in request.json:
        abort(404)

        content = request.get_json(force=True)

        username = content["username"]
        if not username:
            username = slugify(username)

        created_timestamp = datetime.datetime.now()

        user = models.User(username=username, created_timestamp=created_timestamp)

        #open database sesssion
        current_session = db.session

        try:

            current_session.add(user)  # add opened statement to opened session
            current_session.commit()  # commit changes

        except:
            current_session.rollback()
            current_session.flush()  # for resetting non-committed .add()

        finally:
            current_session.close()

    return "OK"




    #     id = db.Column('id', db.Integer, primary_key=True)
    # username = db.Column('username', db.String(28), index=True, unique=True)
    # created_timestamp = db.Column(db.DateTime)
    # files = db.relationship('Files', backref='user')

#
#
# # ------------------------------------------------------
# GET user details
@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
  user = models.User.query.filter(username == username).firt_or_404()
  output = {
      "user": user.username
  }
    return jsonify(output)



# # Delete user
# @app.route('/delete_user/<username>')
# def delete_user(username):
#     pass
#
# # ----------------------------------------------
# # Routes regarding SavedPlaces Table
#
# # get all previous saved places
#
# @app.route('/get_file/', methods=['GET'])
# def getallsavedplaces():
#     """
#     Query data related to all previous saved places and return as a json object
#
#     """
#     pass
#
# # - End of points related to User Table
# # ------------------------------------------------------
# #   POST /create_save_place/ - create a new favorite place place in the database
# @app.route('/create_file/', methods=['POST'])
# def create_saveplace():
#     """
#     :return:
#     """
#     if not request.json or not 'location_lat' in request.json or not 'location_long' in request.json or not 'username' in request.json:
#         abort(404)
#
#
#     return "ok"
#
#
#
# # ----------------------------------------------------------------------
# # route to update the waiting time
#
# @app.route('/update_saved_places/', methods=['POST'])
# def updatesavedplaces():
#     if not request.json or not 'location_lat' in request.json or not 'location_long' in request.json or not 'username' in request.json:
#         abort(404)
#
#
#     return "ok"
#
#
#
#
#
# @app.route('/debugger/')
# def display_debug_message():
#     """Display session and preserves dictionary format in bootbox alert."""
#
#     return jsonify(session)
#
#
#
# # Delete saved place
# @app.route('/delete_saved_place/', method = ['POST'])
# def delete_saved_place():
#     if not request.json or not 'location_lat' in request.json or not 'location_long' in request.json or not 'username' in request.json:
#         abort(404)
#
#     return "ok"
#
#
# # catch page error
# # ----------------------
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
# # -----------------------------
#
# # ----------------------
#
#
#
#

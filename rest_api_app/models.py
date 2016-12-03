from rest_api_app import db

# ----------------------------------
# Database Mapper
# ----------------------------------
class User(db.Model):
    """    Model Table User    """
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(28), index=True, unique=True)
    created_timestamp = db.Column(db.DateTime)
    files = db.relationship('Files', backref='user')

    def __init__(self, username, created_timestamp):

        self.created_timestamp = created_timestamp
        self.username = username

    @property
    def serialize(self):
        #  Return as a json object so it can be used in REST Api
        data = {'id': self.id,
                'username': self.username,
                'created_timestamp': self.created_timestamp}
        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.username, self.created_timestamp)

# ------------------------------------------------------
# Second database Table
# ------------------------------------------------------

class Files(db.Model):
    """
    Model Table Files
    """
    __tablename__ = 'files'
    id = db.Column('id', db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime)
    modified_timestamp = db.Column(db.DateTime)
    file_title = db.Column('file_title', db.String(100))
    file_extension = db.Column('file_extension', db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, created_timestamp, modified_timestamp, file_title, file_extension, user_id):
        self.created_timestamp = created_timestamp
        self.modified_timestamp = modified_timestamp
        self.file_title = file_title
        self.file_extension = file_extension
        self.user_id = user_id

    @property
    def serialize(self):
        #  Return as a json object so it can be used in REST Api
        data = {'user_id': self.user_id,
                'created_timestamp': self.created_timestamp,
                'modified_timestamp': self.modified_timestamp,
                'file_title': self.file_title,
                'file_extension': self.file_extension}
        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(self.user_id, self.created_timestamp, self.modified_timestamp,
                                           self.file_title, self.file_extension)



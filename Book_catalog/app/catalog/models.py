from app import db
from datetime import datetime

class Publication(db.Model):

    __tablename__ = 'Publication'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "the id is {}, name is {}".format(self.id, self.name)

class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False, index = True)
    author = db.Column(db.String(80))
    avg_rating = db.Column(db.Float())
    format = db.Column(db.String(80))
    image = db.Column(db.String(80), unique = True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default = datetime.utcnow())

    #Foreign Key
    pub_id = db.Column(db.Integer, db.ForeignKey('Publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image,  num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image  = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        print("the title {}, author {}, avg_rating {}, format {}, image {}, num_pages{}, pub_id {}".format(self.title, self.author, self.avg_rating,self.format,self.image, self.num_pages,self.pub_id))

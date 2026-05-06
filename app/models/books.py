
from app.extensions import db
from datetime import datetime

class Book(db.Model):
    _tablename_ = 'books' #  table name
    id = db.Column(db.Integer, primary_key = True)    # we automatically inrement ids
    title =  db.Column(db.String(150), nullable =  False)
    pages =  db.Column(db.Integer, nullable = False)
    price =  db.Column(db.Integer, nullable = False)
    price_unit =  db.Column(db.String(50), nullable = False, default = 'UGX')
    publication_date =  db.Column(db.Date, nullable = False)
    isbn =  db.Column(db.String(30), unique = True, nullable = True)# This is an international standard book number
    genre = db.Column(db.String(50), nullable = False)
    description =  db.Column(db.String(255), nullable = False )
    image =  db.Column(db.String(255), nullable = True)
    user_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
    company_id =  db.Column(db.Integer, db.ForeignKey('companies.id'))  # foreign key
    user = db.relationship('User', backref = 'books') # relationship means that they can access the different books they have made
    company = db.relationship('Company', backref = 'books') # A company can have very many books
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())


# constructors
    def _init_(self,title,price,description,pages,user_id,company_id,price_unit,genre,publication_date,isbn,image):
        super(Book,self)._init_() # any necessary initialization from the db.model class is executed before the specific initialization of the book class
        self.title =  title
        self.price = price
        self.description = description
        self.pages = pages
        self.user_id = user_id
        self.price_unit = price_unit
        self.isbn = isbn
        self.publication_date = publication_date
        self.image = image
        self.genre = genre
        self.company_id = company_id



    def _repr_(self)  -> str: # This returns  a string type of an instance that has been created on any model class
        return f"Book {self.title}"



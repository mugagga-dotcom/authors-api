# Define a model class for the user
class Book(db.Model):
   # Using ISBN as a primary key
   isbn = db.Column(db.String(150), primary_key=True)
   title = db.Column(db.String(150))
   author = db.Column(db.String(150))

   @property
   def as_json(self):
       """ Returns object data in a serializable format
       """
       return {
           'isbn': self.isbn,
           'title': self.title,
           'author': self.author
       }
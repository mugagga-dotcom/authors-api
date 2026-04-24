from app.extensions import db
from datetime import datetime

#This handles users for authentication and it is also used for log in and registration
class User(db.Model):
   # Here we are going to customize the table using the table name

   __tablename__="users" 
   id=db.Column(db.Integer,primary_key=True)
   first_name =db.Column(db.String(50),nullable=False) #The first name must not exced 50 characters, it must be a String and cannot be left empty.
   last_name =db.Column(db.String(50),nullable=False)
   email =db.Column(db.String(100),nullable=False, unique=True) # it must be a String and the characters must not exceed 100 and it must be entered once two people cant have the same email.
   contact =db.Column(db.String(50),nullable=False, unique=True)
   image =db.Column(db.String(255),nullable=False, unique=True)
   password =db.Column(db.Text,nullable=False)
   biography =db.Column(db.Text,nullable=True)
   user_type =db.Column(db.String(20), default='author')
   created_at =db.Column(db.DateTime,default=datetime.now())
   updated_at =db.Column(db.DateTime,onupdate=datetime.now())


   def __init__(self,first_name, last_name, email, contact, password, biography,user_type, image=None): #This will help us to reuse the code for another person.
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.contact = contact
      self.password = password
      self.biography = biography
      self.user_type = user_type
      self.image = image

      # function for contacting first name and last name
   def get_full_name(self):
     return f'{self.first_name}{self.last_name}'
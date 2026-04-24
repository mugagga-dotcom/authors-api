from app.extensions import db
from datetime import datetime

class Company(db.Model):
    __tablename__="companies"
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),unique=True)
    origin= db.Column(db.String(100),nullable=False)
    description=db.Column(db.Text(),nullable=False)
    user_id= db.Column(db.integer, db.ForeignKey('users.id'))
    #user =db.relationship('User' backref = 'companies) this will show the relationship b
    created_at =db.Column(db.DateTime,default =datetime.now())
    updated_at=db.Column(db.DateTime,onupdate =datetime.now())

    def __init__(self,name,origin,description,user_id,created_at,updated_at):
        #super().__init__(self,name,origin,description,user_id,created_at,updated_at)
        self.name = name # The ids are automatically implemented thats why we dont pass them
        self.origin = origin
        self.description = description
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
            #return super().__repr__()
            return f"{self.name} {self.origin}"


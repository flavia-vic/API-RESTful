from db import db

class PurchaseOrderModel(db.Model):
    __tablename__ = 'purchase_order'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=True)

    def __init__(self, description):
        self.description = description

    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}
        
    @classmethod
    def find_all(cls):
        return cls.query.all() # select * from table purchase_order


    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first() #select * from purchase_order where id == id


    def save(self):
        db.session.add(self)
        db.session.commit()
    


